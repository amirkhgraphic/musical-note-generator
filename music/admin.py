from django.contrib import admin

from .models import Lab, Generation


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'population_size', 'num_generations', 'mutation_rate', 'best_fitness')
    list_filter = ('user', 'created_at', 'mutation_rate')
    search_fields = ('user__username',)
    readonly_fields = ('best_fitness', 'created_at')
    fieldsets = (
        ('Lab Details', {
            'fields': ('user', 'population_size', 'num_generations', 'mutation_rate'),
        }),
        ('Target and Results', {
            'fields': ('target_sequence', 'best_note', 'best_fitness'),
        }),
        ('Timestamps', {
            'fields': ('created_at',),
        }),
    )
    ordering = ('-created_at',)


@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ('lab', 'number', 'best_fitness', 'created_at')
    list_filter = ('lab', 'created_at')
    search_fields = ('lab__user__username', 'lab__id')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Generation Details', {
            'fields': ('lab', 'number', 'best_note', 'best_fitness'),
        }),
        ('Timestamps', {
            'fields': ('created_at',),
        }),
    )
    ordering = ('lab', 'number')
