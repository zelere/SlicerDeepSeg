import os

import SimpleITK as sitk
from radiomics import featureextractor
import pandas as pd
import six
import joblib
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def feature2pd(image, mask, extractor, mode, label_num):
    print("feature_2pd")
    result = extractor.execute(image, mask, label=label_num)
    sub_dict = {}
    for key, value in six.iteritems(result):
        print('iter')
        if key.find('original') == 0: #篩選key的開頭是'original'
            #print(key)
            #print(float(value))
            key = mode + '_' + key[9:] + '_' + str(label_num)
            value=float(value)
            sub_dict.update({key:value})

    print("subdict", sub_dict)

    return sub_dict

def extract_features(modalities, outputPath, paramsPath, mask):
    print("ExtractFeautures2")
    rel_path = os.path.relpath(paramsPath)
    id_dict = {}
    extractor = featureextractor.RadiomicsFeatureExtractor(rel_path)
    print(extractor)
    results = []
    for mode in modalities.keys():

        print("mode", mode)
        for label_num in [1,2,4]:
            image_1 = sitk.GetImageFromArray(modalities[mode])
            label_1 = sitk.GetImageFromArray(mask)
            try:

                sub_dict = feature2pd(image_1, label_1, extractor, mode, label_num)
                print(sub_dict)
                id_dict.update(sub_dict)
                print("Calculating")

            except:
                print("Non-existing label")

        #print(id_dict)


    print("Out")
    df = pd.DataFrame.from_dict([id_dict])
    print("df")
    print(df)

    return df

def predict_classification(estimator_path, extracted_features):
    est = joblib.load(estimator_path)
    print(est.predict(extracted_features))



    return

