import mlflow

with open("artifacts01.txt") as f:
       text = f.read()


new_text = "end of stage_02"
mlflow.log_param("text",new_text) # key:value
print("end of stage_02")