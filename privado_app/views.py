import json

from http import HTTPStatus
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from privado_app.models import Templates


class HttpResponseNoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT


class HttpResponseBadRequest(HttpResponse):
    status_code = HTTPStatus.BAD_REQUEST


def customer_template_exists(customer_id):
    return Templates.objects.filter(type="customer", customerId=customer_id).exists()


@csrf_exempt
def vw_templates(request, customer_id):

    # validate if customerId is numeric
    if not customer_id.isnumeric():
        # HTTP response code - 400
        return HttpResponseBadRequest(json.dumps({
            'error': 'invalid customerId.'
        }))

    # create template with customerId
    if request.method == "POST":

        # check if customerId already exists
        if customer_template_exists(customer_id):
            return HttpResponseBadRequest(json.dumps({
                'error': 'customerId already exists.'
            }))

        try:
            template = Templates(
                customerId=customer_id, type='customer', entity='entity', law='base', fields=[])
            # append fields from each system records
            for t in Templates.objects.filter(type="system"):
                template.fields += t.fields
            template.save()

            # HTTP response code - 200
            return HttpResponse(json.dumps({
                'type': template.type,
                'entity': template.entity,
                'customerId': template.customerId,
                'law': template.law,
                'fields': template.fields
            }))

        except Templates.DoesNotExist:
            # HTTP response code - 204
            return HttpResponseNoContent(json.dumps({
                'error': 'system records not found.'
            }))

    else:
        try:
            template = Templates.objects.get(
                type="customer", customerId=customer_id)

            # HTTP response code - 200
            return HttpResponse(json.dumps({
                'type': template.type,
                'entity': template.entity,
                'customerId': template.customerId,
                'law': template.law,
                'fields': template.fields
            }))

        except Templates.DoesNotExist:
            # HTTP response code - 204
            return HttpResponseNoContent(json.dumps({
                'error': 'customerId does not exist.'
            }))
