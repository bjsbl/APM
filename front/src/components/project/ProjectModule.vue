<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model.trim="filters.name" placeholder="名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getModuleList">查询</el-button>
        </el-form-item>
       <el-form-item>
        <el-button type='primary' @click='addProjectModule'>新增模块</el-button>
      </el-form-item>
      </el-form>
      </el-col>
    </el-row>
      <el-table :data="projectModuleList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column prop="description" label="描述" sortable></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title="添加模块" :visible.sync="addProjectModuleVisible" :close-on-click-modal="false" >
        <el-form label-width="80px" v-model="moduleForm">
        <el-form-item label='名称'>  
          <el-input type='text' auto-complete="off" v-model.trim="moduleForm.name"></el-input>
        </el-form-item>
        <el-form-item label='描述'>  
          <el-input type="textarea" :rows="5" v-model.trim="moduleForm.description"></el-input>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addProjectModuleVisible = false">取消</el-button>
            <el-button type="primary" @click="addProjectModuleForm" :loading="addLoading">提交</el-button>
          </div>
      </el-dialog>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        listLoading:false,
        addLoading:false,
        moduleListLoading:false,
        addProjectModuleVisible:false,
        moduleList:[],
        projectModuleList:[],
        filters:{
          name:''
        },
        moduleForm:{
          name:'',
          description:''
        }
      }
    },
    methods:{
      getModuleList(){
        let _this = this
        _this.ajax.get("/static/mock/projectmodule.json").then(function(res){
          _this.projectModuleList = res.data.result.data
        })
      },
      addProjectModule(){
        this.addProjectModuleVisible=true
      },
      addProjectModuleForm(){
        this.addProjectModuleVisible=false
      }
    },
    mounted(){
      this.getModuleList()
    }
  }
</script>