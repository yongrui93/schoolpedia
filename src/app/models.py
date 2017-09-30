from django.db import models


class School(models.Model):
    api_id = models.IntegerField(unique=True, blank=True, null=True, default=None)
    school_name = models.CharField(max_length=200)
    url_address = models.TextField()
    address = models.TextField()
    postal_code = models.TextField()
    telephone_no = models.TextField()
    telephone_no_2 = models.TextField()
    fax_no = models.TextField()
    fax_no_2 = models.TextField()
    email_address = models.TextField()
    mrt_desc = models.TextField()
    bus_desc = models.TextField()
    principal_name = models.TextField()
    first_vp_name = models.TextField()
    second_vp_name = models.TextField()
    third_vp_name = models.TextField()
    fourth_vp_name = models.TextField()
    fifth_vp_name = models.TextField()
    visionstatement_desc = models.TextField()
    missionstatement_desc = models.TextField()
    philosophy_culture_ethos = models.TextField()
    dgp_code = models.TextField()
    zone_code = models.TextField()
    cluster_code = models.TextField()
    type_code = models.TextField()
    nature_code = models.TextField()
    session_code = models.TextField()
    mainlevel_code = models.TextField()
    sap_ind = models.TextField()
    autonomous_ind = models.TextField()
    gifted_ind = models.TextField()
    ip_ind = models.TextField()
    mothertongue1_code = models.TextField()
    mothertongue2_code = models.TextField()
    mothertongue3_code = models.TextField()
    special_sdp_offered = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SchedulerLog(models.Model):
    type = models.CharField(
        max_length=2,
        choices=(
            ('N', 'New Entry'),
            ('U', 'Updated Entry')
        )
    )
    school = models.ForeignKey('app.School', blank=True, null=True, default=None)
    field = models.CharField(max_length=30)
    previous_data = models.TextField()
    new_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SchoolComment(models.Model):
    school = models.ForeignKey('app.School')
    description = models.TextField()
    created_by = models.ForeignKey('sso.User')
    created_at = models.DateTimeField(auto_now_add=True)


class Enquiry(models.Model):
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class EnquiryAnswer(models.Model):
    enquiry = models.ForeignKey('app.Enquiry')
    answer = models.TextField()
    answered_by = models.ForeignKey('sso.User')
    created_at = models.DateTimeField(auto_now_add=True)


class Bookmark(models.Model):
    user = models.ForeignKey('sso.User')
    school = models.ForeignKey('app.School')
    created_at = models.DateTimeField(auto_now_add=True)


class CommentReport(models.Model):
    comment = models.ForeignKey('app.SchoolComment')
    reported_by = models.ForeignKey('sso.User')
    created_at = models.DateTimeField(auto_now_add=True)
