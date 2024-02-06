<template>
    <div>
        <el-table :data="tableData.filter(data => !search || data.id.toLowerCase().includes(search.toLowerCase()))" 
            border stripe style="width:100%" height="600" :default-sort = "{prop: 'date', order: 'descending'}">     
            <el-table-column sortable prop="img_name" label="图片名" width="150"></el-table-column>
            <el-table-column sortable prop="model" label="模型" width="100"></el-table-column>
            <el-table-column sortable prop="img_size" label="图片大小" width="110"></el-table-column>
            <el-table-column prop="conf" label="conf" width="100"></el-table-column>
            <el-table-column prop="iou" label="iou" width="100"></el-table-column>
            <el-table-column label="预览" width="200" align="center">
                <template slot-scope="scope">
                    <el-image 
                        style="width: 100px; height: 100px"
                        :src="scope.row.img_donwloadUrl" 
                        :preview-src-list="[scope.row.img_donwloadUrl]">
                    </el-image>
                </template>
            </el-table-column>
            
            <el-table-column align="center" width="200">
                <template slot="header" slot-scope="scope">
                    <el-input v-model="search" size="mini" placeholder="请输入图片名搜索" @focus="scope"/>
                </template>
                <template slot-scope="scope">
                    <el-link :href="scope.row.img_donwloadUrl" type="primary" :underline="false">下载&nbsp;&nbsp;&nbsp;&nbsp;</el-link>
                    <el-link @click="Delete(scope.row.id)" type="primary" :underline="false">&nbsp;&nbsp;&nbsp;&nbsp;删除</el-link>
                </template>
            </el-table-column>  

        </el-table>
    </div>
  
</template>

<script>
export default {
    name:'download',
    data() {
        return {
            tableData: [],
            search: ''
        }
    },
    methods: {
        Delete(row){
            if(confirm("请确定要删除该信息！")){
                this.$axios.post('/deleteImage', {id:row}).then(response => {
                    console.log(response.data)
                    window.location.reload()
                }).error(error => {
                    console.log(error.message)
                    window.location.reload()
                })
            }
        }
    },
	mounted(){
    this.$axios.post('/ImageData',{username:sessionStorage.getItem('username')}).then(response => {
        this.tableData = response.data
        console.log(response.data)
    },error => {
        console.log(error.message)
    })
  },

}
</script>

<style>

</style>