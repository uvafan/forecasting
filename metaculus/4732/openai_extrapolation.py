import numpy as np

def compute(
   start_year: float, 
   start_compute: float, 
   end_year: float, 
   estimation_start_year: float, 
   estimation_start_compute: float
):
    estimation_years = start_year - estimation_start_year
    estimation_compute_doublings = np.log2(start_compute / estimation_start_compute)
    months_to_double = estimation_years * 12 / estimation_compute_doublings

    months = (end_year - start_year) * 12
    doublings = months / months_to_double
    end_compute = start_compute * (2 ** doublings)
    return f"{end_compute:.2E}"


# In this program, a time period ends at the beginning of the stated year
# From https://arxiv.org/pdf/2005.14165.pdf#page=46, GPT-3
start_year = 2020.5
start_compute = 3640

# From https://openai.com/blog/ai-and-compute/, AlphaGo Zero
# start_year = 2018
# start_compute = 1e3

# From https://openai.com/blog/ai-and-compute/, AlexNet
estimation_start_year = 2012.5
estimation_start_compute = .0054

# From https://openai.com/blog/ai-and-compute/, eyeballing graph
# estimation_start_year = 2012
# estimation_start_compute = 1e-4

# The prediction question asks,
# "What will be the compute used in the largest ML training run before 2030"
# https://www.metaculus.com/questions/4732/amplified-forecasting-what-will-bucks-informed-prediction-of-compute-used-in-the-largest-ml-training-run-before-2030-be/#comment-34651
end_year = 2030


print(compute(start_year, start_compute, end_year, estimation_start_year, estimation_start_compute))
