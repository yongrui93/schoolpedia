from app.models import School
from django.shortcuts import render
from app import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect


def school_list(request):
    latitude, longitude, has_coordinate = utils.get_coordinate_from_request(request)

    # queryset and pagination
    queryset = School.objects.all()
    paginator = Paginator(queryset, 10)  # one page contains 10 items
    page = request.GET.get('page')
    try:
        school_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        school_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        school_list = paginator.page(paginator.num_pages)

    compare_school_id_list = request.session.get('compare_school_id_list', [])

    return render(request, 'app/school/school_list.html', {
        'school_list': school_list,
        'allow_compare': len(compare_school_id_list) < 4,
        'has_coordinate': has_coordinate,
        'latitude': latitude,
        'longitude': longitude
    })


def school_detail(request, school_id):
    latitude, longitude, has_coordinate = utils.get_coordinate_from_request(request)
    school = School.objects.get(id=school_id)
    return render(request, 'app/school/school_detail.html', {
        'school': school,
        'has_coordinate': has_coordinate,
        'latitude': latitude,
        'longitude': longitude
    })


def add_to_comparison(request, school_id):
    compare_school_id_list = request.session.get('compare_school_id_list', [])
    if school_id not in compare_school_id_list and len(compare_school_id_list) < 4:
        compare_school_id_list.append(school_id)
    request.session['compare_school_id_list'] = compare_school_id_list
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_comparison(request, school_id):
    compare_school_id_list = request.session.get('compare_school_id_list', [])
    if school_id in compare_school_id_list:
        compare_school_id_list = [x for x in compare_school_id_list if x != school_id]
    request.session['compare_school_id_list'] = compare_school_id_list
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def compare_schools(request):
    compare_school_id_list = request.session.get('compare_school_id_list', [])
    compared_school_list = School.objects.filter(id__in=compare_school_id_list)
    return render(request, 'app/comparison/index.html', {
        'compared_school_list': compared_school_list
    })

def faq(request):
    pass

def contact_us(request):
    if request.method == "POST":
        return HttpResponseRedirect("http://www.google.com")
    else:
        return render(request, 'app/contactus/index.html')

def send_enquiry(contact):
    pass
