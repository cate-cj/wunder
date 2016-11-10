# Weather Underground Data Collector
I was interested in long-term patterns in temperature and precipitation 
and wrote a script to collect data for analysis from 
(Weather Underground)[https://www.wunderground.com]

## Usage
```bash
# today's data for station KYMF (San Diego)
$ python wunder.py kymf

# specific date range (only 12 months max allowed by service)
$ python wunder.py -s 2016-01-01 -e 2016-02-01 kymf

# All 2016 data
$ python wunder.py -y 2016 kymf
```

```bash
#!/usr/bin/env bash

# Collect multiple years
mkdir kymf
for i in {1996..2016}; 
do 
  echo $i
  python wunder.py -y $i kymf > kymf/${i}.csv
done
```

