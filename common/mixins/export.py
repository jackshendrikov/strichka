from import_export.admin import ExportMixin
from import_export.formats.base_formats import CSV, JSON, XLS, XLSX, TextFormat


class CustomExportMixin(ExportMixin):
    """
    Remove unused export formats.
    """

    formats: list[TextFormat] = [
        fmt for fmt in (CSV, XLS, XLSX, JSON) if fmt.is_available()
    ]
