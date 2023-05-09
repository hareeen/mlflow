import transformers
import mlflow

task = "text2text-generation"

generation_pipeline = transformers.pipeline(
    task=task,
    model="declare-lab/flan-alpaca-base",
)

with mlflow.start_run() as run:
    model_info = mlflow.transformers.log_model(
        transformers_model=generation_pipeline,
        artifact_path="text_generator",
        inference_config={"max_length": 512, "do_sample": True},
        input_example=["prompt 1", "prompt 2", "prompt 3"],
    )

sentence_generator = mlflow.pyfunc.load_model(model_info.model_uri)

print(
    sentence_generator.predict(
        ["tell me a story about rocks", "Tell me a joke about a dog that likes spaghetti"]
    )
)