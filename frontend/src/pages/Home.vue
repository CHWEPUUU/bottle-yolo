<template>  
  <div>
    <el-row>
      <!-- 左半边 -->
      <el-col :push="1" :span="12" class="border">
        <div class="img">
          <div v-if="loading" v-loading="loading"
              element-loading-text="正在加载数据，请稍候..." style="padding: 250px"></div>
          <el-image v-else :src="src"></el-image>
      </div></el-col>
      <!-- 右半边 -->
      <el-col :span="12" :push="2">
        <div class="choosebox1">
          <el-row><span>Model</span></el-row>  
          <el-select v-model="model" @change="modelChange(model)">
            <el-option  
              v-for="item in models"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
        <div class="choosebox2">
          <el-row><span>Image Size</span></el-row>  
          <el-select v-model="img_size" @change="img_sizeChange(img_size)">
            <el-option
              v-for="item in img_sizes"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>

        <span class="word">Confidence threshold</span>
        <div class="slider">
          <el-slider v-model="conf" :format-tooltip="formatTooltip" @change="confChange(conf)"></el-slider>
        </div>
        <span class="word">IoU threshold</span>
        <div class="slider">
          <el-slider v-model="iou" :format-tooltip="formatTooltip" @change="iouChange(iou)"></el-slider>
        </div>

        <div class="imglist">
          <el-row style="padding: 0px 0px 10px;">Image examples</el-row>
          <el-row>
            <span v-for="v in imglist" :key="v.src" @click="imglistClick(v.src)">
              <el-col :span="5">
                <!-- 绑定一个动态的 class 来实现只设置选择的图片的边框 -->
                <el-image :class="{'selectedColor': v.src === selectedImg}" style="width: 100px; height: 100px;" v-bind:src="v.src"></el-image>
              </el-col>
            </span>
          </el-row>
        </div>
        
        <div class="word">
          <el-button type="primary" v-on:click="openFile()" round>上传图片</el-button>
          <input type="file" accept="image/*" multiple id="file" style="display:none"/>
        </div>

      </el-col>
    </el-row>

    <div style="text-align: center; padding: 50px 0px 0px 120px"> 
      <el-link href="https://arxiv.org/pdf/2207.02696.pdf" :underline="false">YOLOv7&nbsp;&nbsp;|</el-link> 
      <el-link href="/manage" :underline="false">&nbsp;&nbsp;管理<i class="el-icon-s-tools el-icon--right"></i></el-link> 
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name:'Home',
  data() {
    return {
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg', // 展示图
      selectedSrc:'', // 原图
      selectedImg: '', // 选择的图
      loading: false,
      fileName: '',   
      // models:[{
      //   value: 'yolov7-tiny',
      //   label: 'yolov7-tiny'
      // },{
      //   value: 'yolov7',
      //   label: 'yolov7'
      // }],
      models:[],
      img_sizes: [{
        value: '640',
        label: '640'
      }, {
        value: '320',
        label: '320',
      }],
      img_size: '640',
      model: 'yolov7',

      conf:25,iou:45,

      imglist: [{src:'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'}
        ,{src:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'}
      ]
    }
  },
  methods: {
    formatTooltip(val) {
      return val / 100;
    },
    detect(model, img_size, conf, iou, src) {
      this.loading = true
      // 没有图片就用时间戳代替
      if (this.fileName == '') {
        this.fileName= Date.now().toString() + '.jpg'
      }
      axios.post('/detect', {
        username:sessionStorage.getItem('username'),
        model:model,
        img_size:img_size,
        conf:conf,
        iou:iou,
        img:src,
        fileName:this.fileName
      }).then(response => {
          console.log(response.data)
          this.src = response.data
          this.loading = false;
        },error => {
          console.log(error.message)
          this.loading = false;
        })      
    },
    modelChange(model) {
      console.log(model)
      this.detect(model, this.img_size, this.conf, this.iou, this.selectedSrc)
    },
    img_sizeChange(img_size) {
      console.log(img_size)
      this.detect(this.model, img_size, this.conf, this.iou, this.selectedSrc)
    },
    confChange(conf) {
      console.log(conf)
      this.detect(this.model, this.img_size, conf, this.iou, this.selectedSrc)
    },
    iouChange(iou) {
      console.log(iou)
      this.detect(this.model, this.img_size, this.conf, iou, this.selectedSrc)
    },
    imglistClick(src) {
      this.src = src
      this.selectedSrc = src
      this.selectedImg = src
      this.detect(this.model, this.img_size, this.conf, this.iou, src)
    },
    openFile() {
      var fileInput = document.getElementById("file");
      // 使用箭头函数。箭头函数没有自己的this，它会继承外层函数的this。
      fileInput.onchange = () => {
        // 获取文件路径    
        this.fileName = fileInput.value.split("\\").pop(); // 用反斜杠分割路径，并取最后一部分
        // 在控制台打印文件路径
        console.log(this.fileName);

        axios.post('/upload', {filePath:this.fileName}
            ).then(response => {
                // 将图片存储在sessionStorage中
                let id = 'id' + Date.now().toString();
                sessionStorage.setItem(id, response.data);
                this.imglist.push({src:response.data})
                console.log(response.data)
                this.$notify({
                          title: '图片',
                          message: '上传成功',
                          position: 'bottom-right'});                
                },error => {
                  console.log(error.message)
                })
      };
      fileInput.click();
    },

  },

  mounted() {
    this.$axios.post('/userModels',{username:sessionStorage.getItem('username')})
    .then(response => {
      for(let i = 0; i < response.data.length; i++) {
        this.models.push(
          response.data[i]
        )}
        console.log(response.data)
        console.log(this.models)
    },error => {
        console.log(error.message)
    })
  },
  created() {
    // 遍历sessionStorage中的所有键
    for (let i = 0; i < sessionStorage.length; i++) {   
      if (sessionStorage.key(i).startsWith('id')) {
        // 获取键
        let id = sessionStorage.key(i);
        // 获取值
        let src = sessionStorage.getItem(id);
        // 将id和src添加到imglist数组中
        this.imglist.push({src: src});        
      }      
    }
  },
};
</script>

<style lang="scss" scoped>
  .border {
    border:rgb(41, 41, 40) 5px solid;
    width: 800px;
    height: 700px;
    position: relative;
  }
  .img {
    position: absolute; 
    top: 50%; left: 50%; 
    transform: translate(-50%, -50%);
  }
  .selectedColor { 
    border:5px solid green
  }   
  .choosebox1 {
    padding: 70px 20px 0px;
  }
  .choosebox2  {
    padding: 20px 20px 35px;
  }
  .el-select {
    width: 65%;
  }

  .slider {
    padding: 0px 310px 20px 25px;
  }
  .word {
    padding: 0px 20px 10px;
  }
  .imglist {
    padding: 0px 20px 10px;
  }

  .box {
    padding: 0px 10px 20px 15px;
  }

</style>