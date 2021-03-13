from django_cron import CronJobBase, Schedule

from news.models import News


class ResetUpvotes(CronJobBase):
    RUN_EVERY_MINS = 60 * 12  # every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "news.reset_upvotes"

    def do(self):
        News.objects.filter(amount_of_upvotes__gt=0).update(amount_of_upvotes=0)
