from import_export.admin import ImportExportMixin
from import_export.formats.base_formats import CSV, JSON, XLS, XLSX, TextFormat
from import_export.tmp_storages import CacheStorage


class CustomImportExportMixin(ImportExportMixin):
    """
    Remove unused import_export formats and switched to
    django-import-export's CacheStorage temporary storage method.
    """

    tmp_storage_class = CacheStorage

    formats: list[TextFormat] = [
        fmt for fmt in (CSV, XLS, XLSX, JSON) if fmt.is_available()
    ]
