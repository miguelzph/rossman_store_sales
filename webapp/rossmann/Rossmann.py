import pickle 
import pandas as pd


class InsuranceCrossSell(object):
    
    def __init__(self):
        self.rs_anual_premium = pickle.load(open('../parameters/rs_anual_premium.pkl', 'rb'))
        self.rs_age = pickle.load(open('../parameters/rs_age.pkl', 'rb'))
        self.minmax_vintage = pickle.load(open('../parameters/minmax_vintage.pkl', 'rb'))
        self.encoder_region_code = pickle.load(open('../parameters/encoder_region_code.pkl', 'rb'))
        self.encoder_policy_sales_channel = pickle.load(open('../parameters/encoder_policy_sales_channel.pkl', 'rb'))
        self.encoder_vehicle_age = pickle.load(open('../parameters/encoder_vehicle_age.pkl', 'rb'))
                                        
#     def data_cleaning(self, data1):
        
#         return data1
    
    
    def feature_engineering(self, data2):
        # changing vehicle_damage --> 1 == yes //// 0 == no
        data2['vehicle_damage'] = data2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)

        # vehicle_age
        data2['vehicle_age'] = data2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' 
                                                      else '1_to_2_years' if x == '1-2 Year' 
                                                      else 'under_1_year')
        
        return data2
        
        
    def data_preparation(self, data3):
        data3 = data3.drop(columns=['id'])
        
        # annual_premium
        data3['annual_premium'] = self.rs_anual_premium.transform(data3[['annual_premium']].values)

        # age
        data3['age'] = self.rs_age.transform(data3[['age']].values)

        # vintage
        data3['vintage'] = self.minmax_vintage.transform(data3[['vintage']].values)

        # gender
        data3['gender'] = data3['gender'].apply(lambda x: 1 if x == 'Male' 
                                                      else 0)

        # region_code
        data3['region_code'] = self.encoder_region_code.transform(data3['region_code'].astype(str))


        # policy_sales_channel
        data3['policy_sales_channel'] = self.encoder_policy_sales_channel.transform(data3['policy_sales_channel'].astype(str))


        # vehicle_age
        # One Hot Encoding

        vehicle_age_encoded = self.encoder_vehicle_age.transform(data3['vehicle_age'])
        data3[self.encoder_vehicle_age.get_feature_names()] =  vehicle_age_encoded.values
        data3 = data3.drop(columns=['vehicle_age'])

        
        return data3
    
    def get_prediction(self, model, original_data, prepared_data):
        
        # predictions
        rank = model.predict_proba(prepared_data)
        
        original_data['ranking'] = rank
        
        return original_data.to_json(orient='records', date_format='iso')
        