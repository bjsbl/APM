<template>
  <section>
    <el-row>
      <el-col>
        <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model.trim="filters.name" placeholder="名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getApiList">查询</el-button>
        </el-form-item>
       <el-form-item>
        <el-button type="primary" @click='addApi'>新增接口</el-button>
        <el-button type="primary" @click='importApi'>导入接口</el-button>
        <el-button type="primary" @click='exportApi'>导出接口</el-button>
      </el-form-item>
      </el-form>
      </el-col>
    </el-row>
    <el-table :data="apiList">
      <el-table-column prop="name" label="接口名称"></el-table-column>
      <el-table-column prop="method" label="请求方式"></el-table-column>
      <el-table-column prop="uri" label="接口地址"></el-table-column>
      <el-table-column prop="name" label="最近更新者"></el-table-column>
      <el-table-column prop="lastupdatetime" label="更新日期"></el-table-column>
      <el-table-column prop="status" label="状态">
        <template slot-scope="scope">
          <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="small">编辑</el-button>
          <el-button type="danger" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title='导入接口' :close-on-click-modal='false' :visible.sync='importApiFormStatus'>
      <el-form>
        <el-form-item>  
          <el-upload
            class="upload-demo"
            drag
            action=""
            multiple>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="importApiFormStatus = false">取消</el-button>
            <el-button type="primary" @click="importApiForm" :loading="addLoading">提交</el-button>
          </div>
    </el-dialog>
  </section>
</template>

<script>
  export default{
    data(){
      return{
        apiList:[],
        filters:{name:''},
        addLoading:false,
        importApiFormStatus:false
      }
    },
    methods:{
      getApiList(){
         let _this = this
        _this.ajax.get("/static/mock/apilist.json").then(function(res){
          _this.apiList = res.data.result.data
        })
      },
      addApi(){
        this.$router.push('/api/add/1')
      },
      exportApi(){

      },
      importApi(){
        this.importApiFormStatus=true
      },
      importApiForm(){

      }
    },
    mounted(){
      this.getApiList()
    }
  }
</script>