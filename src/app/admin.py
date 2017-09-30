from django.contrib import admin
from app.models import (
    School,
    SchedulerLog,
    SchoolComment,
    Enquiry,
    EnquiryAnswer,
    Bookmark,
    CommentReport
)


class SchoolAdmin(admin.ModelAdmin):
    list_display = [x.name for x in School._meta.fields]


class SchedulerLogAdmin(admin.ModelAdmin):
    list_display = [x.name for x in SchedulerLog._meta.fields]


class SchoolCommentAdmin(admin.ModelAdmin):
    list_display = [x.name for x in SchoolComment._meta.fields]


class EnquiryAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Enquiry._meta.fields]


class EnquiryAnswerAdmin(admin.ModelAdmin):
    list_display = [x.name for x in EnquiryAnswer._meta.fields]


class BookmarkAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Bookmark._meta.fields]


class CommentReportAdmin(admin.ModelAdmin):
    list_display = [x.name for x in CommentReport._meta.fields]


admin.site.register(School,
                    SchoolAdmin)
admin.site.register(SchedulerLog,
                    SchedulerLogAdmin)
admin.site.register(SchoolComment,
                    SchoolCommentAdmin)
admin.site.register(Enquiry,
                    EnquiryAdmin)
admin.site.register(EnquiryAnswer,
                    EnquiryAnswerAdmin)
admin.site.register(Bookmark,
                    BookmarkAdmin)
admin.site.register(CommentReport,
                    CommentReportAdmin)
