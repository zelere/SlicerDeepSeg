import os
from radiomics import featureextractor
import sys

def extract_features(inputDict, outputPath, paramsPath):
    print("ExtractFeautrures")

    rel_path = os.path.relpath(paramsPath)





    extractor = featureextractor.RadiomicsFeatureExtractor(rel_path)
    print(extractor)
    for file in inputDict:
        print(file)
            # image_path = os.path.join(root, file)
            # image_1 = sitk.ReadImage(image_path)
            # label = file.split('.')[0].rsplit('_', 1)[0] + '_seg.nii'
            # label_path = os.path.join(root, file)
            # label_1 = sitk.ReadImage(label_path)
            # merged_label = sitk.ConnectedComponent(label_1)
            # result_1 = extractor.execute(image_1, merged_label)
            # result_1['image_id'] = image_id
            # result_1['mode'] = mode.strip('.')
            # results.append(result_1)

    # df = pd.DataFrame.from_records(results)
    # df.to_csv(os.path.join(result_folder, mode.strip('.') + '_features.csv'))
    # return os.path.join(result_folder, mode.strip('.') + '_features.csv')