import mlflow


def main():
       with mlflow.start_run() as run:
              mlflow.run(".","stage_01",use_conda=False)
              mlflow.run(".","stage_02",use_conda=False)
              mlflow.run(".","stage_03",use_conda=False)

              '''
              run_stage_03 = input("run stage 03 or not? [y/n]")
              if run_stage_03 == "y":
                     mlflow.run(".","stage_03",use_conda=False)
              '''


if __name__ =="__main__":
       main()