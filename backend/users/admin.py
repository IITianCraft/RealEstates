from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.template.defaultfilters import truncatechars

from .models import (
    CustomUser,
    Property,
    PropertyImage,
    SavedProperty,
    MeetingRequest,
    Notification,
    EventPlace,  
    EventPlaceImage, 
    EventBooking 
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email',
        'name',
        'phone',
        'user_type',
        'is_staff',
        'is_active',
        'gender',
        'birth_date',
        'date_joined',
        'last_login',
    )
    list_filter = (
        'is_staff',
        'is_active',
        'gender',
        'user_type',
        'date_joined',
    )
    search_fields = ('email', 'name', 'phone')
    ordering = ('-date_joined',) # Order by newest users first

    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'password')
        }),
        ('Personal Info', {
            'fields': ('phone', 'user_type', 'bio', 'gender', 'birth_date', 'profile_pic')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined') # Include date_joined here
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'name', 'password', 'password2',
                'phone', 'user_type',
                'bio', 'gender', 'birth_date', 'profile_pic',
                'is_staff', 'is_active', 'is_superuser'
            )
        }),
    )
    

admin.site.register(CustomUser, CustomUserAdmin)


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1 

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user_link',
        'location',
        'price',
        'property_type',
        'status',
        'created_at',
        'admin_actions',
    )
    list_filter = (
        'status',
        'property_type',
        'type',
        'furnished',
        'created_at',
    )
    search_fields = (
        'title',
        'location',
        'description',
        'contact_name',
        'user__email',
        'user__name',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [PropertyImageInline]
    raw_id_fields = ('user',) 

    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'description', 'location')
        }),
        ('Details', {
            'fields': ('price', 'type', 'furnished', 'property_type', 'bedrooms', 'bathrooms', 'area')
        }),
        ('Contact Information', {
            'fields': ('contact_name', 'contact_phone', 'contact_email')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )

    actions = [
        'make_active',
        'make_pending',
        'make_inactive',
    ]

    @admin.action(description='Mark selected properties as Active')
    def make_active(self, request, queryset):
        updated = queryset.update(status='Active')
        self.message_user(request, f'{updated} properties marked as Active.')

    @admin.action(description='Mark selected properties as Pending')
    def make_pending(self, request, queryset):
        updated = queryset.update(status='Pending')
        self.message_user(request, f'{updated} properties marked as Pending.')

    @admin.action(description='Mark selected properties as Inactive')
    def make_inactive(self, request, queryset):
        updated = queryset.update(status='Inactive')
        self.message_user(request, f'{updated} properties marked as Inactive.')

    def user_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.user.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.user.email))
    user_link.short_description = 'Owner'
    user_link.admin_order_field = 'user__email'

    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">View on site</a>', 
            reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk]),
            '#' 
        )
    admin_actions.short_description = 'Actions'



@admin.register(SavedProperty)
class SavedPropertyAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'property_link', 'saved_at')
    list_filter = ('saved_at',)
    search_fields = ('user__email', 'user__name', 'property__title', 'property__location')
    raw_id_fields = ('user', 'property') # Improve performance for FKs
    date_hierarchy = 'saved_at'
    ordering = ('-saved_at',)

    def user_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.user.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.user.email))
    user_link.short_description = 'User'
    user_link.admin_order_field = 'user__email'

    def property_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, Property._meta.model_name), args=[obj.property.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.property.title))
    property_link.short_description = 'Property'
    property_link.admin_order_field = 'property__title'


@admin.register(MeetingRequest)
class MeetingRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user_link',
        'property_link',
        'proposed_time_slot',
        'status',
        'requested_at',
        'truncated_purpose',
    )
    list_filter = (
        'status',
        'proposed_time_slot',
        'requested_at',
    )
    search_fields = (
        'user__email',
        'user__name',
        'property__title',
        'meeting_purpose',
    )
    date_hierarchy = 'proposed_time_slot'
    ordering = ('-requested_at',)
    raw_id_fields = ('user', 'property')

    actions = [
        'mark_pending',
        'mark_accepted',
        'mark_rejected',
        'mark_completed',
    ]

    @admin.action(description='Mark selected requests as Pending')
    def mark_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} meeting requests marked as Pending.')

    @admin.action(description='Mark selected requests as Accepted')
    def mark_accepted(self, request, queryset):
        updated = queryset.update(status='accepted')
        self.message_user(request, f'{updated} meeting requests marked as Accepted.')

    @admin.action(description='Mark selected requests as Rejected')
    def mark_rejected(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} meeting requests marked as Rejected.')

    @admin.action(description='Mark selected requests as Completed')
    def mark_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} meeting requests marked as Completed.')

    def user_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.user.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.user.email))
    user_link.short_description = 'Requester'
    user_link.admin_order_field = 'user__email'

    def property_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, Property._meta.model_name), args=[obj.property.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.property.title))
    property_link.short_description = 'Property'
    property_link.admin_order_field = 'property__title'

    def truncated_purpose(self, obj):
        return truncatechars(obj.meeting_purpose, 50)
    truncated_purpose.short_description = 'Purpose'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'notification_type', 'truncated_message', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('user__email', 'user__name', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('user',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    actions = [
        'mark_as_read',
        'mark_as_unread',
        'delete_selected_notifications',
    ]

    @admin.action(description='Mark selected notifications as read')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} notifications marked as read.')

    @admin.action(description='Mark selected notifications as unread')
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} notifications marked as unread.')

    @admin.action(description='Delete selected notifications')
    def delete_selected_notifications(self, request, queryset):
        deleted_count, _ = queryset.delete()
        self.message_user(request, f'{deleted_count} notifications deleted.')
    
    def user_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.user.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.user.email))
    user_link.short_description = 'Recipient'
    user_link.admin_order_field = 'user__email'

    def truncated_message(self, obj):
        return truncatechars(obj.message, 70)
    truncated_message.short_description = 'Message'



class EventPlaceImageInline(admin.TabularInline):
    model = EventPlaceImage
    extra = 1

@admin.register(EventPlace)
class EventPlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner_link',
        'location',
        'price_per_hour',
        'capacity',
        'category',
        'is_available_now',
        'status',
        'created_at',
        'admin_actions', 
    )
    list_filter = (
        'status',
        'category',
        'is_available_now',
        'created_at',
    )
    search_fields = (
        'name',
        'location',
        'description',
        'contact_name',
        'owner__email',
        'owner__name',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [EventPlaceImageInline]
    raw_id_fields = ('owner',)

    fieldsets = (
        (None, {
            'fields': ('owner', 'name', 'description', 'location')
        }),
        ('Details', {
            'fields': ('price_per_hour', 'capacity', 'category', 'is_available_now')
        }),
        ('Contact Information', {
            'fields': ('contact_name', 'contact_phone', 'contact_email')
        }),
        ('Admin Status', {
            'fields': ('status',)
        }),
    )

    actions = [
        'set_status_active',
        'set_status_pending_review',
        'set_status_inactive',
        'mark_available',
        'mark_unavailable',
    ]

    @admin.action(description='Set status to Active')
    def set_status_active(self, request, queryset):
        updated = queryset.update(status='active')
        self.message_user(request, f'{updated} event places set to Active.')

    @admin.action(description='Set status to Pending Review')
    def set_status_pending_review(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} event places set to Pending Review.')

    @admin.action(description='Set status to Inactive')
    def set_status_inactive(self, request, queryset):
        updated = queryset.update(status='inactive')
        self.message_user(request, f'{updated} event places set to Inactive.')

    @admin.action(description='Mark selected as Available Now')
    def mark_available(self, request, queryset):
        updated = queryset.update(is_available_now=True)
        self.message_user(request, f'{updated} event places marked as Available Now.')

    @admin.action(description='Mark selected as Unavailable Now')
    def mark_unavailable(self, request, queryset):
        updated = queryset.update(is_available_now=False)
        self.message_user(request, f'{updated} event places marked as Unavailable Now.')
    
    def owner_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.owner.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.owner.email))
    owner_link.short_description = 'Owner'
    owner_link.admin_order_field = 'owner__email'

    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">View on site</a>',
            reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk]),
            '#'
        )
    admin_actions.short_description = 'Actions'


@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = (
        'event_place_link',
        'user_link',
        'booking_date',
        'start_time',
        'end_time',
        'number_of_guests',
        'event_type',
        'total_cost',
        'status',
        'booked_at',
    )
    list_filter = (
        'status',
        'booking_date',
        'event_place__category', # Filter by event place category
        'event_type',
    )
    search_fields = (
        'user__email',
        'user__name',
        'event_place__name',
        'event_place__location',
        'event_type',
    )
    date_hierarchy = 'booking_date'
    ordering = ('-booked_at',)
    raw_id_fields = ('user', 'event_place')
    
    actions = [
        'mark_booking_pending',
        'mark_booking_confirmed',
        'mark_booking_cancelled',
        'mark_booking_completed',
    ]

    @admin.action(description='Mark selected bookings as Pending')
    def mark_booking_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} bookings marked as Pending.')

    @admin.action(description='Mark selected bookings as Confirmed')
    def mark_booking_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} bookings marked as Confirmed.')

    @admin.action(description='Mark selected bookings as Cancelled')
    def mark_booking_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} bookings marked as Cancelled.')

    @admin.action(description='Mark selected bookings as Completed')
    def mark_booking_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} bookings marked as Completed.')

    def user_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, CustomUser._meta.model_name), args=[obj.user.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.user.email))
    user_link.short_description = 'Booked By'
    user_link.admin_order_field = 'user__email'

    def event_place_link(self, obj):
        link = reverse("admin:%s_%s_change" % (obj._meta.app_label, EventPlace._meta.model_name), args=[obj.event_place.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.event_place.name))
    event_place_link.short_description = 'Event Place'
    event_place_link.admin_order_field = 'event_place__name'