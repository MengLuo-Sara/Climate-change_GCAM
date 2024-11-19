# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:33:41 2024

@author: mluo46
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]: read packages and paths


import os, platform
import time


## computer
# root = "O:/E/"
# out_path = "Data/"

## computer NAS
root = "Z:/Meng/Chapter 2/"
out_path = "experiment/Data/"


## old laptop
# root = "C:/My/climate_FPC_GCAM/"
# out_path = "Data/"

# ctrl+1 batch comment
if platform.system() == "Windows" :
    # Since python 3.8 it will no longer use the PATH environment
    # variable to find DLLs on Windows.
    # The recommended alternative is to use os.add_dll_directory
    # however it means we have to insert system specific info into
    # our .py script.  TODO: find a better solution 
    
   # ## computer
   # os.add_dll_directory("C:/Program Files/Java/jdk-11.0.11/bin")
   # os.add_dll_directory("C:/Program Files/Java/jdk-11.0.11/bin/server")
   # os.add_dll_directory("O:/E/GCAMv7Forestry-master_VS/GCAMv7Forestry-master/exe")

   ## computer NAS
   os.add_dll_directory("C:/Program Files/Java/jdk-11.0.11/bin")
   os.add_dll_directory("C:/Program Files/Java/jdk-11.0.11/bin/server")
   os.add_dll_directory("Z:/Meng/Chapter 2/backup/GCAMv7Forestry-master_VS/GCAMv7Forestry-master/exe")

   ## my old laptop
   #os.add_dll_directory("C:/Program Files/Java/jdk-17/bin")
   #os.add_dll_directory("C:/Program Files/Java/jdk-17/bin/server")
   #os.add_dll_directory("C:/My/climate_FPC_GCAM/GCAMv7Forestry-master_VS/exe")
   
   ## laptop
   
   # os.add_dll_directory("C:/Program Files/Java/jdk-20/bin")
   # os.add_dll_directory("C:/Program Files/Java/jdk-20/bin/server")    
   # os.add_dll_directory("D:/E/GCAMv7Forestry-master_VS/GCAMv7Forestry-master/exe")
   # Now that we can find the DLLs, we will be able to load our
   # package
   
   
import gcamwrapper
##########################
# Ctrl + / batch comment




import pandas as pd
# import gcamwrapper

# Ctrl + / batch comment

# In[3]
## computer 
# in_exe_path = os.path.join(root, "GCAMv7Forestry-master_VS/GCAMv7Forestry-master/exe")
## computer NAS
in_exe_path = os.path.join(root, "backup/GCAMv7Forestry-master_VS/GCAMv7Forestry-master/exe")
## old laptop
# in_exe_path = os.path.join(root, "GCAMv7Forestry-master_VS/exe")

start_time2 = time.time()
##########################
#g = gcamwrapper.Gcam("configuration_ref.xml", in_exe_path)
g = gcamwrapper.Gcam("configuration_policy_ssp126_usetax_ag_cost_prodchange_classic_ukesm_orifor2.xml", in_exe_path)
new_db_name = "SSP126_classic_ukesm_allupdate_db_v3_nege3_orifor_n3"
#######################################

end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[4]: read the new agb data updated by C scaler & filter the needed year's data
## computer
# common_CD_path = os.path.join(root, "new laptop2/PHD/phd_dissertation/climate_FPC_GCAM/Data/ISIMIP3b_processed/GCAM_subregion_mean/")

## computer NAS
common_CD_path = os.path.join(root, "experiment/GCAM_subregion_mean/")
## old laptop
# common_CD_path = os.path.join(root, "Data/GCAM_carbondensity/")

# read new agb
new_agb_path = os.path.join(common_CD_path, "annual_wmean_aboveCD/region_5ymean_alltypes_wrapper_5level/")
agb_file_path_l1 = os.path.join(new_agb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_agb_l1_v3.csv')
agb_file_path_l2 = os.path.join(new_agb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_agb_l2_v3.csv')
agb_file_path_l3 = os.path.join(new_agb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_agb_l3_ori_for_v3.csv')
agb_file_path_l5 = os.path.join(new_agb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_agb_l5_v3.csv')
# Reading the CSV with headers
agb_new_l1 = pd.read_csv(agb_file_path_l1)
agb_new_l2 = pd.read_csv(agb_file_path_l2)
agb_new_l3 = pd.read_csv(agb_file_path_l3)
agb_new_l5 = pd.read_csv(agb_file_path_l5)
# Display the DataFrame
print(agb_new_l5.head())

# read new bgb
new_bgb_path = os.path.join(common_CD_path, "annual_wmean_belowCD/region_5ymean_alltypes_wrapper_5level/")
bgb_file_path_l1 = os.path.join(new_bgb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_bgb_l1_v3.csv')
bgb_file_path_l2 = os.path.join(new_bgb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_bgb_l2_v3.csv')
bgb_file_path_l3 = os.path.join(new_bgb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_bgb_l3_ori_for_v3.csv')
bgb_file_path_l5 = os.path.join(new_bgb_path, 'classic_ukesm1-0-ll_w5e5_ssp126_2015soc-from-histsoc_default_c34_concise_bgb_l5_v3.csv')
# Reading the CSV with headers
bgb_new_l1 = pd.read_csv(bgb_file_path_l1)
bgb_new_l2 = pd.read_csv(bgb_file_path_l2)
bgb_new_l3 = pd.read_csv(bgb_file_path_l3)
bgb_new_l5 = pd.read_csv(bgb_file_path_l5)
# Display the DataFrame
print(bgb_new_l5.head())

## the query for agb and bgb
# agb
agb_query = gcamwrapper.get_query("land", "above_carbon_density")

agb_query_1level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes{leaf@name}/carbon-calc/above-ground-carbon-density'
agb_query_2level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/above-ground-carbon-density'
agb_query_3level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/above-ground-carbon-density'
# because this query will get 0 rows of data
#agb_query_4level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/above-ground-carbon-density'
agb_query_5level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/above-ground-carbon-density'


# bgb
bgb_query = gcamwrapper.get_query("land", "below_carbon_density")
bgb_query_1level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes{leaf@name}/carbon-calc/below-ground-carbon-density'
bgb_query_2level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/below-ground-carbon-density'
bgb_query_3level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/below-ground-carbon-density'
# because this query will get 0 rows of data
#bgb_query_4level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/below-ground-carbon-density'
bgb_query_5level = 'world/region{region@name}/land-allocator/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes/child-nodes{leaf@name}/carbon-calc/below-ground-carbon-density'

# In[5-0]: urun to 2015
period=2015

start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")
# In[5]: use unrolling methods to filter & set agb 2020 
period=2020
## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[6]: filter & set agb 2025 
period=2025

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[7]: filter & set agb 2030
period=2030

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[8]: filter & set agb 2035
period=2035

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[9]: filter & set agb 2040
period=2040

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[10]: filter & set agb 2045
period=2045

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[11]: filter & set agb 2050
period=2050

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[12]: filter & set agb 2055
period=2055

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[13]: filter & set agb 2060
period=2060

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[14]: filter & set agb 2065
period=2065

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[15]: filter & set agb 2070
period=2070

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[16]: filter & set agb 2075
period=2075

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[17]: filter & set agb 2080
period=2080

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[18]: filter & set agb 2085
period=2085

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[19]: filter & set agb 2090
period=2090

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[20]: filter & set agb 2095
period=2095

## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")

## run this time step
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

# In[21]: run till
period=2100
## filter data for this time step
t1 = time.time()
# agb
agb_new_l1_1step = agb_new_l1[agb_new_l1['year'] == period].drop(columns='year')
agb_new_l2_1step = agb_new_l2[agb_new_l2['year'] == period].drop(columns='year')
agb_new_l3_1step = agb_new_l3[agb_new_l3['year'] == period].drop(columns='year')
agb_new_l5_1step = agb_new_l5[agb_new_l5['year'] == period].drop(columns='year')
# bgb
bgb_new_l1_1step = bgb_new_l1[bgb_new_l1['year'] == period].drop(columns='year')
bgb_new_l2_1step = bgb_new_l2[bgb_new_l2['year'] == period].drop(columns='year')
bgb_new_l3_1step = bgb_new_l3[bgb_new_l3['year'] == period].drop(columns='year')
bgb_new_l5_1step = bgb_new_l5[bgb_new_l5['year'] == period].drop(columns='year')

end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to filter agb and bgb.")

## set data
# agb
t1 = time.time()
g.set_data(agb_new_l1_1step, agb_query_1level)
g.set_data(agb_new_l2_1step, agb_query_2level)
g.set_data(agb_new_l3_1step, agb_query_3level)

g.set_data(agb_new_l5_1step, agb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set agb.")


# bgb
t1 = time.time()
g.set_data(bgb_new_l1_1step, bgb_query_1level)
g.set_data(bgb_new_l2_1step, bgb_query_2level)
g.set_data(bgb_new_l3_1step, bgb_query_3level)

g.set_data(bgb_new_l5_1step, bgb_query_5level)
end_time = time.time()
# Calculate the duration
duration = end_time - t1
print(f"The command took {duration} seconds to set bgb.")
#########################
start_time2 = time.time()
g.run_period(g.convert_year_to_period(period))
end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2

# save new db

new_db_path = os.path.join(root, out_path, new_db_name)
g.print_xmldb(new_db_path)

end_time2 = time.time()
# Calculate the duration
duration2 = end_time2 - start_time2
print(f"The command took {duration2} seconds to run.")

