<template>
  <section>
    <el-row>
      <el-col :span="24">
        <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model.trim="filters.name" placeholder="名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getProjectList">查询</el-button>
        </el-form-item>
       <el-form-item>
        <el-button type='primary' @click='addProject'>新增项目</el-button>
        <el-button type='primary' @click='defaultViewType=!defaultViewType' 
        icon="el-icon-menu">切换</el-button>
      </el-form-item>
      </el-form>
      </el-col>
    </el-row>
    <el-row :gutter="10">
      <el-col :span='18'>
        <transition name="el-fade-in-linear">
        <el-row v-show="defaultViewType">
          <el-col :span="8" v-for="project in projectList" :key='index'>
            <el-card>
                版本：{{project.version}}
              <div style="padding: 14px;">
                <span>{{project.name}}</span>
                <div class="bottom clearfix">
                  <time class="time">{{project.lastUpdateTime}}</time>
                </div>
                <el-button-group>
                  <el-button size="small" class="button">关注</el-button>
                  <el-button size="small" class="button">编辑</el-button>
                  <el-button size="small" class="button">删除</el-button>
                  <el-button size="small" class="button">状态</el-button>
                  <el-button size="small" class="button">导出</el-button>
                </el-button-group>
              </div>
          </el-card>
          </el-col>
        </el-row>
      </transition>
      <transition name="el-fade-in-linear">
    <el-table :data='projectList'  v-show="!defaultViewType">
      <el-table-column label='项目名称' prop='name'>
        <template slot-scope="scope">
          <router-link :to="'/module/'+scope.row.id">
            {{ scope.row.name }}
          </router-link>
        </template> 
      </el-table-column>
      <el-table-column label='版本' prop='version'></el-table-column>
      <el-table-column label='状态' prop='status'>
        <template slot-scope="scope">
            <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
        </template>
      </el-table-column>
      <el-table-column label='关注' prop='star'>
        <template slot-scope="scope">
          <el-button type="warning" v-show="scope.row.star" icon="el-icon-star-on" circle></el-button>
          <el-button type="warning" v-show="!scope.row.star" icon="el-icon-star-off" circle></el-button>
        </template>
      </el-table-column>
      <el-table-column label='最后修改时间' prop='lastUpdateTime'></el-table-column>
      <el-table-column label='导出'>
        <template slot-scope="scope">
          <el-button size="small">PDF</el-button>
        </template>
      </el-table-column>
      <el-table-column label='操作'>
        <template slot-scope="scope">
          <el-button-group>
          <el-button size="small">编辑</el-button>
          <el-button type="danger" size="small" @click='goDel'>删除</el-button>
        </el-button-group>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination background layout="prev, pager, next" :page-size="10" :page-count="total"></el-pagination>
  </transition>
    </el-col>
    <el-col :span='6'>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>最新动态</span> 
        </div>
        <div v-for='item in dynamic' class="item text">
          <i class="el-icon-time"></i>{{item.createTime}} <i class="el-icon-caret-right"></i>{{item.description}}
        </div>
      </el-card>
    </el-col>
    </el-row>

    <el-dialog title='新增' :close-on-click-modal='false' :visible.sync='addProjectFormStatus'>
      <el-form label-width="80px" v-model="projectListForm">
        <el-form-item label='项目名称'>  
          <el-input type='text' auto-complete="off" v-model.trim="projectListForm.name"></el-input>
        </el-form-item>
        <el-form-item label='版本号'>  
          <el-input type='text' auto-complete="off" v-model.trim="projectListForm.version"></el-input>
        </el-form-item>
        <el-form-item label='描述'>  
          <el-input type="textarea" :rows="5" v-model.trim="projectListForm.description"></el-input>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addProjectFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addProjectForm" :loading="addLoading">提交</el-button>
          </div>
    </el-dialog>
  </section>
</template>

<script>
  export default{
    data(){
      return {
        total:0,
        projectList:[],
        dynamic:[],
        addLoading:false,
        addProjectFormStatus:false,
        defaultViewType:false,
        filters:{
          name:''
        },
        projectListForm:{
          name:'',
          version:'',
          description:''
        }
      }
    },
    methods:{
      getProjectList(){
        let _this = this
        _this.ajax.get("/static/mock/project.json").then(function(res){
          _this.projectList = res.data.result.data
        })
      },
      getDynamic(){
        let _this = this
        _this.ajax.get("/static/mock/dynamic.json").then(function(res){
          _this.dynamic = res.data.result.data
        })
      },
      addProject(){
        this.addProjectFormStatus = true
      },
      addProjectForm(){
        this.addProjectFormStatus = false
        this.$notify({
          title: '成功',
          message: '这是一条成功的提示消息',
          type: 'success'
        });
      },
      goApiList(){

      },
      goDel(){
        this.$confirm('确认关闭？')
          .then(_ => {
            this.$notify({
              title: '成功',
              message: '这是一条成功的提示消息',
              type: 'success'
            });
          })
          .catch(_ => {});
      }
    },
    mounted(){
      this.getProjectList()
      this.getDynamic()
    }
  }

</script>
<style>
  .text{
     font-size: 14px;
  }
  .item {
    margin-bottom: 18px;
  }
</style>