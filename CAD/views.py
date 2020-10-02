from django.http import HttpResponseRedirect
from django.shortcuts import render
from CAD import forms, tool_list
from CAD.models import Shaft, Hole, Lambda, IT


def index(request):
    return render(request, 'CAD/index.html')


def lang(request):
    return render(request, 'CAD/index.html')


def tol(request):
    if request.method == 'POST':
        form = forms.TolerancesForm(request.POST)
        diameter = request.POST['diameter']
        feature_type = request.POST['feature_type']
        tolerance_class = request.POST['tolerance_class']
        tolerance_letter = request.POST['tolerance_letter']

        it_pre_filtered = IT.objects.filter(dia_max__gte=diameter)
        it_filtered = it_pre_filtered.filter(dia_min__lt=diameter)

        if tolerance_class == '1':
            it_result = [line.IT1 for line in it_filtered]
        elif tolerance_class == '2':
            it_result = [line.IT2 for line in it_filtered]
        elif tolerance_class == '3':
            it_result = [line.IT3 for line in it_filtered]
        elif tolerance_class == '4':
            it_result = [line.IT4 for line in it_filtered]
        elif tolerance_class == '5':
            it_result = [line.IT5 for line in it_filtered]
        elif tolerance_class == '6':
            it_result = [line.IT6 for line in it_filtered]
        elif tolerance_class == '7':
            it_result = [line.IT7 for line in it_filtered]
        elif tolerance_class == '8':
            it_result = [line.IT8 for line in it_filtered]
        elif tolerance_class == '9':
            it_result = [line.IT9 for line in it_filtered]
        elif tolerance_class == '10':
            it_result = [line.IT10 for line in it_filtered]
        elif tolerance_class == '11':
            it_result = [line.IT11 for line in it_filtered]
        elif tolerance_class == '12':
            it_result = [line.IT12 for line in it_filtered]
        elif tolerance_class == '13':
            it_result = [line.IT13 for line in it_filtered]
        elif tolerance_class == '14':
            it_result = [line.IT14 for line in it_filtered]
        elif tolerance_class == '15':
            it_result = [line.IT15 for line in it_filtered]
        elif tolerance_class == '16':
            it_result = [line.IT16 for line in it_filtered]
        elif tolerance_class == '17':
            it_result = [line.IT17 for line in it_filtered]
        elif tolerance_class == '18':
            it_result = [line.IT18 for line in it_filtered]
        else:
            it_result = []

        if feature_type == 'shaft':
            shaft_pre_filtered = Shaft.objects.filter(dia_max__gte=diameter)
            shaft_filtered = shaft_pre_filtered.filter(dia_min__lt=diameter)

            if tolerance_letter == 'a':
                shaft_result = [line.a for line in shaft_filtered]
            elif tolerance_letter == 'c':
                shaft_result = [line.c for line in shaft_filtered]
            elif tolerance_letter == 'd':
                shaft_result = [line.d for line in shaft_filtered]
            elif tolerance_letter == 'e':
                shaft_result = [line.e for line in shaft_filtered]
            elif tolerance_letter == 'f':
                shaft_result = [line.f for line in shaft_filtered]
            elif tolerance_letter == 'g':
                shaft_result = [line.g for line in shaft_filtered]
            elif tolerance_letter == 'h':
                shaft_result = [line.h for line in shaft_filtered]
            elif tolerance_letter == 'j':
                shaft_result = [line.j for line in shaft_filtered]
            elif tolerance_letter == 'k':
                shaft_result = [line.d for line in shaft_filtered]
            elif tolerance_letter == 'm':
                shaft_result = [line.m for line in shaft_filtered]
            elif tolerance_letter == 'n':
                shaft_result = [line.n for line in shaft_filtered]
            elif tolerance_letter == 'p':
                shaft_result = [line.p for line in shaft_filtered]
            elif tolerance_letter == 'r':
                shaft_result = [line.r for line in shaft_filtered]
            elif tolerance_letter == 's':
                shaft_result = [line.s for line in shaft_filtered]
            else:
                shaft_result = []
            es = shaft_result[0]
            ei = es - it_result[0]


        else:

            lambda_pre_filtered = Lambda.objects.filter(dia_max__gte=diameter)
            lambda_filtered = lambda_pre_filtered.filter(dia_min__lt=diameter)

            if tolerance_class == '3':
                lambda_result = [line.IT3 for line in lambda_filtered]
            elif tolerance_class == '4':
                lambda_result = [line.IT4 for line in lambda_filtered]
            elif tolerance_class == '5':
                lambda_result = [line.IT5 for line in lambda_filtered]
            elif tolerance_class == '6':
                lambda_result = [line.IT6 for line in lambda_filtered]
            elif tolerance_class == '7':
                lambda_result = [line.IT7 for line in lambda_filtered]
            elif tolerance_class == '8':
                lambda_result = [line.IT8 for line in lambda_filtered]
            else:
                lambda_result = []

            hole_pre_filtered = Hole.objects.filter(dia_max__gte=diameter)
            hole_filtered = hole_pre_filtered.filter(dia_min__lt=diameter)

            if tolerance_letter == 'a':
                hole_result = [line.a for line in hole_filtered]
            elif tolerance_letter == 'c':
                hole_result = [line.c for line in hole_filtered]
            elif tolerance_letter == 'd':
                hole_result = [line.d for line in hole_filtered]
            elif tolerance_letter == 'e':
                hole_result = [line.e for line in hole_filtered]
            elif tolerance_letter == 'f':
                hole_result = [line.f for line in hole_filtered]
            elif tolerance_letter == 'g':
                hole_result = [line.g for line in hole_filtered]
            elif tolerance_letter == 'h':
                hole_result = [line.h for line in hole_filtered]
            elif tolerance_letter == 'j':
                hole_result = [line.j for line in hole_filtered]
            elif tolerance_letter == 'k':
                hole_result = [line.d for line in hole_filtered]
            elif tolerance_letter == 'm':
                hole_result = [line.m for line in hole_filtered]
            elif tolerance_letter == 'n':
                hole_result = [line.n for line in hole_filtered]
            elif tolerance_letter == 'p':
                hole_result = [line.p for line in hole_filtered]
            elif tolerance_letter == 'r':
                hole_result = [line.r for line in hole_filtered]
            elif tolerance_letter == 's':
                hole_result = [line.s for line in hole_filtered]
            else:
                hole_result = []
            ei = hole_result[0]
            if tolerance_letter == 'k' or tolerance_letter == 'm' or tolerance_letter == 'n':
                ei = ei + lambda_result[0]
            es = ei + it_result[0]

        return render(request, 'CAD/tol.html', {'form': form, 'feature_type': feature_type,
                                                'diameter': diameter, 'ei': ei, 'es': es})
    else:
        form = forms.TolerancesForm()
        return render(request, 'CAD/tol.html', {'form': form, })


def grp(request):
    return render(request, 'CAD/index.html')


def tool(request):
    form = forms.UploadFileForm()
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            tool_list.tool_list(request.FILES['file'])
        form = forms.UploadFileForm()
        import PEK.settings
        new_path = PEK.settings.STATIC_URL
        info = '<div class="alert alert-dark" role="alert">' \
               'Tool List created successfully!<br>' \
               f'<a href="{new_path}CAD/TOOL_LIST.MIN" download>Download</a></div>'
        return render(request, 'CAD/tool_list.html', {'form': form, 'info': info, })
    else:
        form = forms.UploadFileForm()
        return render(request, 'CAD/tool_list.html', {'form': form, })
