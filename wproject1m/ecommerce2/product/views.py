# from django.views import ListView
import csv, io

import pandas as pd
import numpy as np

import random
# from django.contrib.auth.models import User
# from django.shortcuts import render
# from .filters import UserFilter

from django_pandas.io import read_frame

from django.core.paginator import Paginator
from tablib import Dataset
from product.resources import ProductResource
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# Create your views here.
from carts.models import Cart
from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "product/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "product/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return product.objects.featured()

class ProductListView(ListView):
    #queryset = product.objects.all()
    template_name = "product/list.html"

    def get_queryset(self, *args, **kwargs ):
        request = self.request
        return Product.objects.all()


    def product_list_view(request):
        queryset = Product.objects.all()
        # queryset2 = Product.objects.filter(category="Accessory")

        context = {
            "object_list": queryset
        }

        return render(request, "product/list.html", context)

    def phone_list_view(request):
        queryset_list = Product.objects.filter(category="Phone").order_by('-price')
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)


        context = {
            "object_list": queryset
        }

        return render(request, "product/list.html", context)

    from django.core.paginator import Paginator
    from django.shortcuts import render

    def accessories_view(request):
        queryset_list = Product.objects.filter(category="Accessory")
        queryset1 = Product.objects.all().values('title','price','Average_Rating','Review_count')

        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        context = {
            "object_list": queryset,
            "aobject_list": queryset1
        }
        return render(request, "product/list.html", context)

    def samsung(request):
        queryset_list = Product.objects.filter(title__icontains="Samsung").order_by('-price')
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def huawei(request):
        queryset_list = Product.objects.filter(title__icontains="huawei").order_by('-price')
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def apple(request):
        queryset_list = Product.objects.filter(title__icontains="apple").order_by('-price')
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def less_than_10k(request):
        queryset_list = Product.objects.filter(price__lte="10000")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def RangeOf10k20k(request):
        queryset_list = Product.objects.filter(price__range=(10000, 20000))
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def RangeOf20k30k(request):
        queryset_list = Product.objects.filter(price__range=(20000, 30000))
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def greater_than_30k(request):
        queryset_list = Product.objects.filter(price__gte="30000")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def One_GB(request):
        queryset_list = Product.objects.filter(Ram__icontains="1GB")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Two_GB(request):
        queryset_list = Product.objects.filter(Ram__icontains="2GB")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Three_GB(request):
        queryset_list = Product.objects.filter(Ram__icontains="3GB")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Four_GB(request):
        queryset_list = Product.objects.filter(Ram__icontains="4GB")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Five_MP(request):
        queryset_list = Product.objects.filter(Main__icontains="5MP")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Eight_MP(request):
        queryset_list = Product.objects.filter(Main__icontains="8MP")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def Twelve_MP(request):
        queryset_list = Product.objects.filter(Main__icontains="12MP")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def TwelveMore_MP(request):
        queryset_list = Product.objects.filter(Main__icontains="12MP")
        paginator = Paginator(queryset_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)
        context = {
            "object_list": queryset
        }
        return render(request, "product/list.html", context)

    def pproduct_view(request):

        current_average = []
        current_review_count = []
        predicted_products = []
        predicted_products_result = []

        qs = Product.objects.all()

        queryset = Product.objects.all().values('title','price','Average_Rating','Review_count')
        # print(queryset)
        for avg in queryset:
            current_average.append(float(avg['Average_Rating']))
            current_review_count.append(float(avg['Review_count']))

        print(current_average)
        average_result = sum(current_average)/len(current_average)
        print(average_result)

        minimum_criteria = np.quantile(current_review_count, 0.7)
        print(minimum_criteria)

        for avr,rc in zip(current_average,current_review_count):
            print(avr,"  ",rc)
            predicted_products = (rc / (rc + minimum_criteria) * avr) + (minimum_criteria / (minimum_criteria + rc) * average_result)
            print(avr," ",rc," ",predicted_products)
            predicted_products_result.append(predicted_products)


        print(predicted_products)



        # Product.Populrity_Score.append('predicted_products')

        queryset = Product.objects.all()

        # print(len(queryset))
        for value, p in enumerate(queryset):
            obj = Product.objects.get(id=p.id)
            obj.Populrity_Score=predicted_products_result[value]
            obj.save()

        # print(queryset)

        # obj = Product('Populrity_Score')

        queryset1_list = Product.objects.order_by('-Populrity_Score')
        print(queryset1_list)
        paginator = Paginator(queryset1_list, 12)  # Show 25 contacts per page
        page = request.GET.get('page')
        queryset_final = paginator.get_page(page)



        context = {

            "object_list": queryset_final
        }

        return render(request, "product/list.html", context)

    def phome(request):
        products = Product.objects.all()
        pridected_products = []
        sum_average_rating = 0
        no_of_user_list = []

        for p in products:
            rating = Product.objects.filter(product_id=p.product_id)

            count = 1
            result = 0

            for r in rating:
                result = result + int(r.product_rating_id.product_rating_id)
                count = count + 1

            if count == 1:
                pass
            else:
                count = count - 1

            average_rating = round(result / count)
            sum_average_rating = sum_average_rating + average_rating
            no_of_user_list.append(count)

            image = Product.objects.filter(product_id=p.product_id)
            image_count = image.count()
            try:
                image = image[image_count - 1].product_image.url
            except:
                pass

            pridected_products.append(
                {"p_id": p.product_id, "p_title": p.product_title, "p_price": p.product_selling_price,
                 "p_avg_rating": average_rating, "p_image": image, "no_users_rating": count, "weighted_rating": 0})

        try:
            mean_rating = sum_average_rating / products.count()
        except:
            pass
        minimum_criteria = np.quantile(no_of_user_list, 0.8)
        print(minimum_criteria)

        for pp in pridected_products:
            weighted_rating = (
                    (pp["no_users_rating"] / (pp["no_users_rating"] + minimum_criteria)) * pp["p_avg_rating"] +
                    (pp["no_users_rating"] / (pp["no_users_rating"] + minimum_criteria)) * pp["no_users_rating"]
            )
            pp["weighted_rating"] = weighted_rating
            if pp["no_users_rating"] < minimum_criteria:
                pridected_products.remove(pp)

        pridected_products = sorted(pridected_products, key=lambda k: k['weighted_rating'], reverse=True)
        pridected_products = pridected_products[:25]
        try:
            pridected_products = random.sample(pridected_products, 8)
        except:
            pass

        ctx = {"products": pridected_products}
        return render(request, 'index.html', ctx)


    def Popular(request):
        products = Product.objects.all()

        predicted_products = []
        No_of_user = []

        for p in products:
            rating = Product.objects.filter(product_id=p.product_id)

            count = 1
            result = 0

            for r in rating:
                result = result + int(r.product_id.product_id)
                count = count + 1

            if count == 1:
                pass
            else:
                count = count - 1

        No_of_user.append(count)


        for p in products:
            predicted_products.append({"Product_id": p.id, "p_title": p.title, "p_price": p.price,
                 "p_avg_rating": p.Average_Rating, "p_image": p.image, "no_users_rating": p.Review_count, "weighted_rating": 0})


        minimum_criteria =np.quantile(No_of_user,0.7)
        print(minimum_criteria)

        for pp in predicted_products:
            weighted_rating = (
                    (pp["no_users_rating"]/(pp["no_users_rating"]+minimum_criteria))*pp["p_avg_rating"] +
                (pp["no_users_rating"]/(pp["no_users_rating"]+minimum_criteria))*pp["no_users_rating"]
                           )

            pp["weighted_rating"] = weighted_rating
            if pp["no_users_rating"] < minimum_criteria:
                predicted_products.remove(pp)


        predicted_products = sorted(predicted_products, key=lambda k: k['weighted_rating'], reverse=True)
        predicted_products = predicted_products[:25]

        # try:
        #     predicted_products = random.sample(predicted_products, 8)
        # except:
        #     pass


        context={

            "products" : predicted_products


        }

        return render(request, "products/plist.html",context)



class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        #instance = get_object_or_404(product , slugs=slug, active=True)

        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance=qs.first()
        except:
            raise Http404("Uhmm")

        return instance


class ProductDetailView(DetailView):
    #queryset = product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request =self.request
        pk = self.kwargs.get("pk")
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("product doesn't exist")


    context = {
        "object": instance
    }
    return render(request, "product/detail.html", context)


@permission_required('admin.can_add_log_entry')
def product_upload(request):
    template = 'product_upload.html'

    prompt = {
        'order': 'Order of our csv should be like your model'
    }


    if request.method == 'GET':
        return render(request, template , prompt)

    csv_file= request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,"this is not a csv file")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=",", quotechar="|" ):
       _, created = Product.objects.update_or_create(
            title = column[0],
            slug=column[1],
            category=column[2],
            price=column[3],
            Charging=column[4],
            Torch=column[5],
            Games=column[6],
            Messaging=column[7],
            Browser=column[8],
            Audio=column[9],
            Data=column[10],
            NFC=column[11],
            USB =column[12],
            GPS=column[13],
            Bluetooth=column[14],
            Wifi=column[15],
            Front=column[16],
            Main=column[17],
            card=column[18],
            BuiltIn=column[19],
            Features=column[20],
            Protection=column[21],
            Resolution=column[22],
            Size=column[23],
            Technology=column[24],
            GPU=column[25],
            Chipset=column[26],
            CPU=column[27],
            FourGBand=column[28],
            ThreeGBand=column[29],
            TwoGBand=column[30],
            Color=column[31],
            SIM=column[32],
            Weight=column[33],
            Dimension=column[34],
            UIBuild=column[35],
            OperatingSystem=column[36],
            image=column[37],
            image1=column[38],
            image2=column[39],
            Review_count=column[40],
            Average_Rating=column[41],
            Reviews=column[42],
            Ram=column[43],
            Populrity_Score=column[44],
            Knowledge_Score=column[45],
            # featured=column[46],
            # active=column[47],
            # timestamp=column[48],


        )

    context ={}
    return render(request, template, context)

def advanced_search(request):
    template = 'product/snippets/search_form.html';
    context = {}
    return render(request, template, context)

def simple_upload(request):
    if request.method == 'POST':
        person_resource = ProductResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')