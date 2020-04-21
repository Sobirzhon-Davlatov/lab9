from api.views import company_list, get_company, vacancy_list, vacancy_topList, company_vacancy

from django.urls import path

urlpatterns = [
  path('companies/', company_list),
  path('companies/<int:c_id>',get_company),
  path('companies/<int:c_id>/vacancies/', company_vacancy),
  path('vacancies/', vacancy_list),
  path('vacancies/top_ten/', vacancy_topList)

]
