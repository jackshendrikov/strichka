from django.core.exceptions import ValidationError
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError as SchemaValidationError
from rest_framework.serializers import ModelSerializer

from common.models.base import StrichkaBaseModel


def validate_form_with_schema(
    schema: type[BaseModel], serializer: type[ModelSerializer], model: StrichkaBaseModel
) -> None:
    """
    Validate model form using schema.
    """
    serialized_model = serializer(model)
    model_data = serialized_model.data
    model_data.update({"id": model.pk})
    model.is_cleaned = True

    try:
        schema.parse_obj(model_data)
    except SchemaValidationError as base_error:
        fields_names = set(serialized_model.fields.keys())
        validation_errors = {}

        for error in base_error.errors():
            field = error["loc"][0]
            msg = error["msg"]

            if model.pk is not None and ("No changes" in msg or "already exist" in msg):
                # Not checking uniques for already existing model.
                continue

            # Show errors for visible fields only.
            if field in fields_names:
                validation_errors[field] = msg

        if validation_errors:
            raise ValidationError(message=validation_errors)
