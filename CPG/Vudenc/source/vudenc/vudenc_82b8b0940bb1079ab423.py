@property...
if self.child_branch:
return '{} ({} {})'.format(self.child.title, self.relative_credits or self.
    child_branch.credits or 0, _('credits'))
components = LearningComponentYear.objects.filter(
    learningunitcomponent__learning_unit_year=self.child_leaf).annotate(total
    =Case(When(hourly_volume_total_annual=None, then=0), default=F(
    'hourly_volume_total_annual'))).values('type', 'total')
return '{} {} [{}] ({} {})'.format(self.child_leaf.acronym, self.child.
    complete_title_english if self.child.complete_title_english and 
    translation.get_language() == 'en' else self.child.complete_title,
    volume_total_verbose(components), self.relative_credits or self.
    child_leaf.credits or 0, _('credits'))
