protocol 'jdbc:derby:';
connect 'jobs.db';
readonly on;

-- use this for old executions

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select CREATION, DOWNLOAD-QUEUED,
RUNNING-DOWNLOAD, UPLOAD-RUNNING, END_E-UPLOAD from jobs where
EXIT_CODE=0', 'timeline.dat', ',', '"', 'UTF-8');


