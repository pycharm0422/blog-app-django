# from django.contrib import admin
# from .models import Posts, Profile
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


# admin.site.register(Posts)
# admin.site.register(Profile)



# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'




# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_occupation')
#     list_select_related = ('profile', )

#     def get_occupation(self, instance):
#         return instance.profile.occupation
#     get_occupation.short_description = 'Occupation'

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)




# # class CustomUserAdmin(UserAdmin):
# #     inlines = (ProfileInline, )

# #     def get_inline_instances(self, request, obj=None):
# #         if not obj:
# #             return list()
# #         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from .models import Posts, Profile, Comments

admin.site.register(Posts)
admin.site.register(Profile)
admin.site.register(Comments)