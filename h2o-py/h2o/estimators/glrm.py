from .estimator_base import H2OEstimator


class H2OGLRMEstimator(H2OEstimator):
  def __init__(self,k=None, max_iterations=None, transform=None, seed=None,
               ignore_const_cols=None,loss=None, multi_loss=None, loss_by_col=None,
               loss_by_col_idx=None, regularization_x=None, regularization_y=None,
               gamma_x=None, gamma_y=None, init_step_size=None, min_step_size=None,
               init=None, svd_method=None, user_x=None, user_y=None, recover_svd=None):
    super(H2OGLRMEstimator, self).__init__()
    self.parms = locals()
    self.parms = {k:v for k,v in self.parms.iteritems() if k!="self"}
    self.parms["algo"]="glrm"
    self.parms['_rest_version']=99


def glrm(k=None,max_iterations=None,transform=None,seed=None,
         ignore_const_cols=None,loss=None,multi_loss=None,loss_by_col=None,loss_by_col_idx=None,regularization_x=None,
         regularization_y=None,gamma_x=None,gamma_y=None,init_step_size=None,min_step_size=None,init=None,svd_method=None,
         user_y=None,user_x=None,recover_svd=None):
  """
  Builds a generalized low rank model of a H2O dataset.

  Parameters
  ----------
  k : int
    The rank of the resulting decomposition. This must be between 1 and the number of columns in the training frame inclusive.
  max_iterations : int
    The maximum number of iterations to run the optimization loop. Each iteration consists of an update of the X matrix, followed by an
    update of the Y matrix.
  transform : str
    A character string that indicates how the training data should be transformed before running GLRM.
    Possible values are "NONE": for no transformation, "DEMEAN": for subtracting the mean of each column, "DESCALE": for
    dividing by the standard deviation of each column, "STANDARDIZE": for demeaning and descaling, and "NORMALIZE": for
    demeaning and dividing each column by its range (max - min).
  seed : int
    (Optional) Random seed used to initialize the X and Y matrices.
  ignore_const_cols : bool, optional
    A logical value indicating whether to ignore constant columns in the training frame. A column is constant if all of its
    non-missing values are the same value.
  loss : str
    A character string indicating the default loss function for numeric columns. Possible values are "Quadratic" (default), "Absolute", "Huber",
    "Poisson", "Hinge", and "Logistic".
  multi_loss : str
    A character string indicating the default loss function for enum columns. Possible values are "Categorical" and "Ordinal".
  loss_by_col : str
    (Optional) A list of strings indicating the loss function for specific columns by corresponding index in loss_by_col_idx.
    Will override loss for numeric columns and multi_loss for enum columns.
  loss_by_col_idx : str
    (Optional) A list of column indices to which the corresponding loss functions in loss_by_col are assigned. Must be zero indexed.
  regularization_x : str
    A character string indicating the regularization function for the X matrix. Possible values are "None" (default), "Quadratic",
    "L2", "L1", "NonNegative", "OneSparse", "UnitOneSparse", and "Simplex".
  regularization_y : str
    A character string indicating the regularization function for the Y matrix. Possible values are "None" (default), "Quadratic",
    "L2", "L1", "NonNegative", "OneSparse", "UnitOneSparse", and "Simplex".
  gamma_x : float
    The weight on the X matrix regularization term.
  gamma_y : float
    The weight on the Y matrix regularization term.
  init_step_size : float
    Initial step size. Divided by number of columns in the training frame when calculating the proximal gradient update. The algorithm
    begins at init_step_size and decreases the step size at each iteration until a termination condition is reached.
  min_step_size : float
    Minimum step size upon which the algorithm is terminated.
  init : str
    A character string indicating how to select the initial X and Y matrices.
    Possible values are "Random": for initialization to a random array from the standard normal distribution, "PlusPlus": for initialization
    using the clusters from k-means++ initialization, "SVD": for initialization using the first k (approximate) right singular vectors, and
    "User": user-specified initial X and Y frames (must set user_y and user_x arguments).
  svd_method : str
    A character string that indicates how SVD should be calculated during initialization.
    Possible values are "GramSVD": distributed computation of the Gram matrix followed by a local SVD using the JAMA package,
    "Power": computation of the SVD using the power iteration method, "Randomized": approximate SVD by projecting onto a random subspace.
  user_x : H2OFrame
    (Optional) An H2OFrame object specifying the initial X matrix. Only used when init = "User".
  user_y : H2OFrame
    (Optional) An H2OFrame object specifying the initial Y matrix. Only used when init = "User".
  recover_svd : bool
    A logical value indicating whether the singular values and eigenvectors should be recovered during post-processing of the generalized
    low rank decomposition.


  :return: a new dim reduction model
  """
  parms = {k:v for k,v in locals().items() if k in ["training_frame", "validation_frame", "validation_x", "validation_y", "offset_column", "weights_column", "fold_column"] or v is not None}
  parms["algo"]="glrm"
  parms['_rest_version']=99
  return h2o_model_builder.unsupervised(parms)
