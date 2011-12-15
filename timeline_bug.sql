protocol 'jdbc:derby:';
connect 'jobs.db';
readonly on;

-- use this for local executions

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select CREATION, QUEUED-CREATION,
DOWNLOAD, RUNNING, UPLOAD from jobs where EXIT_CODE=0',
'timeline.dat', ',', '"', 'UTF-8');

-- latency calculation

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select QUEUED-CREATION from jobs 
where EXIT_CODE=0', 'queued.dat', ',', '"', 'UTF-8');

-- global statistics

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select count(RUNNING) from jobs
where COMMAND like ''mask%'' and EXIT_CODE=0', 'patients.dat', ',',
'"', 'UTF-8');

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select count(RUNNING) from jobs
where COMMAND like ''fsl%'' and EXIT_CODE=0', 'images.dat', ',', '"',
'UTF-8');

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select max(CREATION +
QUEUED-CREATION + DOWNLOAD + RUNNING + UPLOAD) from jobs where
EXIT_CODE=0', 'timespan.dat', ',', '"', 'UTF-8');

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select RUNNING from jobs where
EXIT_CODE=0', 'running.dat', ',', '"', 'UTF-8');

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select count(RUNNING) from jobs',
'total.dat', ',', '"', 'UTF-8');
