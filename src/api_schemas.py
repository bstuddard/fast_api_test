from pydantic import BaseModel


# Define input and output schema
class TextClassificationInput(BaseModel):
    input_text_list: list[str]


class ResponseDict(BaseModel):
    output: dict[str, dict[str, float]]

    class Config:
        schema_extra = {
            "example": {
                "output": {
                    "Great food!": {
                        "negative": 0.0030399556271731853,
                        "neutral": 0.02544713392853737,
                        "positive": 0.9715129137039185
                    },
                    "Horrible food!": {
                        "negative": 0.974818229675293,
                        "neutral": 0.020662227645516396,
                        "positive": 0.004519559442996979
                    }
                }
            }
        }