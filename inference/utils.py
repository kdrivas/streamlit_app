import cv2

def load_model(path):
	return cv2.dnn.readNetFromTorch(path)

def get_models(model_path):
	names = [
		"candy",
		"composition_vii",
		"feathers",
		"la_muse",
		"mosaic",
		"the_scream",
		"udnie",
	]
	models = {}
	for model_name in names:
		models[model_name] = load_model(f'{model_path}/{model_name}.t7')

	return models