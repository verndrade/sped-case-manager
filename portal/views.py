from django.shortcuts import render

# GET /
def index(request):
    return render(request, 'index.html')

# GET /casemanager
def case_manager_landing_page(request):
    return render(request, 'casemanager.html')

# GET /casemanager/student
def student(request):
    return render(request, 'student.html')

# GET /casemanager/student/assignments
def assignments(request):
    return render(request, 'assignments.html')

# GET /casemanager/student/iep
def iep(request):
    return render(request, 'iep.html')

# GET /casemanager/student/discipline
def discipline(request):
    return render(request, 'discipline.html')