import vue from 'vue'
//npm i vuex@3
import vuex from 'vuex'
import user from './user'
vue.use(vuex)

export default new vuex.Store({
    modules:{
        user,
    }
})
