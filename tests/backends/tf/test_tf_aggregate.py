import tensorflow as tf
from sklearn.metrics import roc_auc_score

import crossfit as cf

# from crossfit.ml.classification import BinaryClassificationState
from crossfit.backends.tf.metrics import to_tf_metric


auc = cf.create_mean_metric(roc_auc_score)

# class BinaryMetrics(cf.Aggregator):
#     state = BinaryClassificationState

#     def prepare(self, labels, predictions, sample_weight=None):
#         predictions = np.array(predictions > 0.5, np.int32)
#         # Calculate true-positives
#         tp = np.sum((predictions == 1) & (labels == 1))

#         # Calculate true-negatives
#         tn = np.sum((predictions == 0) & (labels == 0))

#         # Calculate false-positives
#         fp = np.sum((predictions == 1) & (labels == 0))

#         # Calculate false-negatives
#         fn = np.sum((predictions == 0) & (labels == 1))

#         return BinaryClassificationState(tp, tn, fp, fn)

#     def present(self, state: BinaryClassificationState):
#         # Somehow a keras metric is not allowed to return a dict
#         #   See: https://github.com/keras-team/keras/issues/16665
#         return {
#             # "accuracy": state.accuracy,
#             # "precision": state.precision,
#             # "recall": state.recall,
#             # "f1": state.f1,
#             "auc": state.auc,
#         }


def test_to_tf_metric():
    aggregator = auc
    metric = to_tf_metric(aggregator)

    # generate some random tensors
    preds = tf.random.uniform((10,))
    targets = tf.random.uniform((10,), maxval=2, dtype=tf.int32)
    metric.prepare(targets, preds)

    results = metric(targets, preds)
    assert isinstance(results, tf.Tensor)