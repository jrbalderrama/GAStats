protocol 'jdbc:derby:';
connect 'jobs.db';
readonly on;

CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY('select CREATION, QUEUED, DOWNLOAD,
RUNNING, UPLOAD, END_E from jobs where
EXIT_CODE=0','timeline.dat',',','"','UTF-8');

