from django.contrib import admin
from django.utils.html import format_html
from .models import HeroSection, Goal, SkillCategory, Skill, Project, Education, ContactInfo


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero (Top Section)', {
            'fields': ('tagline', 'profile_image', 'cta_text', 'cta_link')
        }),
        ('About Section', {
            'fields': ('bio_paragraph1', 'bio_paragraph2')
        }),
    )

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('text', 'order')
    list_editable = ('order',)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'level', 'proficiency', 'years_of_experience', 'icon', 'order', 'is_active']
    ordering = ['order']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'skill_count']
    list_editable = ['order']
    search_fields = ['name']
    inlines = [SkillInline]
    
    def skill_count(self, obj):
        return obj.skills.filter(is_active=True).count()
    skill_count.short_description = "Active Skills"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency_badge', 'level_bar', 'years_of_experience', 'order', 'is_active']
    list_filter = ['category', 'proficiency', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'category__name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'icon')
        }),
        ('Skill Level', {
            'fields': ('proficiency', 'level', 'years_of_experience'),
            'description': 'Proficiency determines the recommended level range'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def proficiency_badge(self, obj):
        colors = {
            'beginner': '#9e9e9e',
            'intermediate': '#2196f3',
            'advanced': '#ff9800',
            'expert': '#4caf50'
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 11px;">{}</span>',
            colors.get(obj.proficiency, '#9e9e9e'),
            obj.get_proficiency_display()
        )
    proficiency_badge.short_description = "Proficiency"
    
    def level_bar(self, obj):
        return format_html(
            '<div style="width: 100px; background: #f0f0f0; border-radius: 10px; overflow: hidden;">'
            '<div style="width: {}%; background: #4caf50; color: white; text-align: center; '
            'border-radius: 10px; font-size: 11px; line-height: 18px;">{}</div></div>',
            obj.level, obj.level
        )
    level_bar.short_description = "Level"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'link', 'order')
    list_editable = ('order',)
    fields = ('title', 'description', 'tags', 'link', 'link_label', 'image', 'order')
    help_texts = {
        'tags': 'Separate with commas e.g. Django, Python, CSS',
    }


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'year_start', 'year_end', 'order')
    list_editable = ('order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Message', {'fields': ('intro_text',)}),
        ('Social Links', {'fields': ('email', 'linkedin_url', 'github_url', 'instagram_url')}),
    )
    
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()