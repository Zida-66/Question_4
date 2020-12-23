import pandas as pd
import numpy as np
from skimage import data, color, morphology, feature, measure, color


data = pd.read_csv(input_question_4.txt',header=None)
x_list = np.array(data).reshape((10,-1))
x_list = measure.label(x_list,connectivity=1)  # 1 stands for 4-connectivity，2 stands for 8-connectivity
pd.DataFrame(x_list).to_csv('output_question_4.txt', index=False, header=None)