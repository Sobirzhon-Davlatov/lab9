import json
from  django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from api.models import Company, Vacancy

@csrf_exempt
def company_list(request):
  if request.method == 'GET':
    companies = Company.objects.all()
    companies_json = [copan.to_json() for copan in companies ]
    return JsonResponse(companies_json,safe=False)

  elif request.method == 'PUT':
    request_body = json.loads(request.body)

    company = Company.objects.create(name=request_body['name'], description=request_body['description'], address=request_body['address'], city=request_body['city'])
    return JsonResponse(company.short())

 # companies = Company.objects.all()
  #company_json = [c.to_json() for c in companies]
  #return JsonResponse(company_json, safe=False)


@csrf_exempt
def get_company(request, c_id):
  try:

    companies_id = Company.objects.get(id=c_id)
  except Company.DoesNotExist as e:
    return JsonResponse({'error': str(e)})

  if request.method =='GET':
    return JsonResponse(companies_id.to_json())
  elif request.method =='PUT':
     request_body =  json.loads(request.body)
     companies_id.name = request_body.get('name',companies_id.name)
     companies_id.save()
     return JsonResponse(companies_id.to_json())

  elif request.method =='DELETE':
    companies_id.delete()
    return JsonResponse(companies_id.to_json())
  return JsonResponse(companies_id.to_json())







def vacancy_list(request):
  vacancies = Vacancy.objects.all()
  vacancy_json = [v.to_json() for v in vacancies]
  return JsonResponse(vacancy_json, safe=False)


def vacancy_topList(request):
  vacancies1 = Vacancy.objects.all().order_by('-salary')
  vacancies1_json = [vacancy.to_json() for vacancy in vacancies1]
  return JsonResponse(vacancies1_json, safe=False)


def company_vacancy(request, c_id):
  try:
    comp = Company.objects.get(id=c_id)
  except Company.DoesNotExist as e:
    return JsonResponse({'error': str(e)})
  vacancies= comp.vacancy_set.all()
  vacancies1_json = [vacan.to_json() for vacan in vacancies]

  return JsonResponse(vacancies1_json, safe= False)
