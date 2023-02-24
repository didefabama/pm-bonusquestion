import chartmogul
import json

config = chartmogul.Config('MY API KEY HERE')


# Parameters
start_date = '2019-01-01'
end_date = '2019-04-01'
interval = 'month'

# Retrieve MRR 
mrr_promise = chartmogul.Metrics.mrr(config,start_date=start_date, end_date=end_date, interval=interval)
mrr_entries = mrr_promise.get().entries

# Format and print MRR data
total_q1_mrr = sum([m.mrr for m in mrr_entries])
print(f'Total MRR for Q1 2019: ${total_q1_mrr/100:.2f}')

for m in mrr_entries:
    print(f'{m.date.strftime("%B")}: ${m.mrr/100:.2f}')




