module.exports = {
  apps : [{
    name:'FastAPI',
    script: 'uvicorn main:app --reload --host 0.0.0.0',
    cwd: './scrapPDET/',
    merge_logs: true,
    combine_logs: true,
    out_file: "logs/api.log",
    error_file: "logs/api.log",

  }, {
    name: 'Vue.ts',
    script: 'yarn serve',
    cwd: './webapp/',
    merge_logs: true,
    combine_logs: true,
    out_file: "logs/front.log",
    error_file: "logs/front.log",
  }],
};
