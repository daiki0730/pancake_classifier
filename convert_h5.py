import coremltools

coreml_model = coremltools.converters.keras.convert(
'pancake_cnn_aug.h5',
input_names='image',
image_input_names='image',
output_names='Prediction',
class_labels=["pancake","salad","yakiniku"],)
coreml_model.save('/Users/daiki/pancake_classifier/pancake_cnn_aug.mlmodel')
