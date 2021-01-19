from django.contrib import admin

from ..admin import librarian
from .models import BookLoan, Library


class BookLoanInline(admin.StackedInline):
    model = BookLoan
    extra = 1
    readonly_fields = ("id", "duration")
    fields = (
        "book",
        "imprint",
        "status",
        "due_back",
        "borrower",
        "loan_start",
        "duration",
    )


@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "borrower", "due_back", "id")
    list_filter = ("status", "due_back")

    # The User model needs to be registered to be able to make borrower
    # an autocomplete field. In the library view, user management isn't
    # available.
    # In real life, we can completely swap out one ModelAdmin to better
    # fit the needs of a specific user group. Here, I'm lazy and just
    # comment it out as an autocomplete for all admin sites. :)
    #autocomplete_fields = ("borrower",)

    search_fields = ("book__title",)
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back", "duration", "borrower")}),
    )

    def response_change(self, request, obj):
        ret = super().response_change(request, obj)

        if "reserve" in request.POST:
            obj.status = "r"
            obj.save()
        return ret


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "librarian")


# Register a limited set of models to the custom admin site for librarians:
admin.register(BookLoan, site=librarian)(BookLoanAdmin)
