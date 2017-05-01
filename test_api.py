#from amazon.api import AmazonAPI
import amazonproduct
from amazonproduct import API
api = API(locale='de')


## Credentials
access_key = 'AKIAIOWFZ4KTTJAKNLFQ'
secret_key = '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'
associate_tag = 'q0d9b-20'


amazon = AmazonAPI(access_key, secret_key, associate_tag)
products = amazon.search_n(1, Keywords='earphone', SearchIndex='All')
len(products)


#Amazon Credentials: Associate ID: q0d9b-20
#Access Key: AKIAIOWFZ4KTTJAKNLFQ
#Secret Access Code: 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
