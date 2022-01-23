module.exports = {
  apps : [{
    name:'FastAPI',
    script: 'uvicorn main:app --reload --host 0.0.0.0',
    cwd: './scrapPDET/'
  }, {
    name: 'Vue.js',
    script: 'yarn serve',
    cwd: './basic-test/'
  }],
};
