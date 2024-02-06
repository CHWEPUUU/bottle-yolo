module.exports = {
    pages:{
        index:{
            entry:'src/main.js',
        },
    },
    lintOnSave:false,

    devServer:{
        //后端URL
        proxy:'http://localhost:8081/'
    }
}