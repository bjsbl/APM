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
          <el-button type="primary" @click="getCaseResultList">查询</el-button>
        </el-form-item>
      </el-form>
      </el-col>
    </el-row>
      <el-table :data="caseResultList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="用例">
          <template slot-scope="scope">
            <router-link :to="'/case/api'">{{scope.row.name }}</router-link>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="项目"></el-table-column>
        <el-table-column prop="description" label="通过">
          <template slot-scope="scope">
            <el-progress :text-inside="true" :stroke-width="18" :percentage="60"></el-progress>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="失败">
          <template slot-scope="scope">
            <el-progress :text-inside="true" :stroke-width="18" :percentage="60"></el-progress>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="异常">
          <template slot-scope="scope">
            <el-progress :text-inside="true" :stroke-width="18" :percentage="60"></el-progress>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="时间"></el-table-column>
        <el-table-column prop="description" label="日志">
          <template slot-scope="scope">
            <el-button type="primary" size="small">查看日志</el-button>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="报告">
          <template slot-scope="scope">
            <el-button-group>
            <el-button type="primary" size="small">用例报告</el-button>
            <el-button type="primary" size="small">性能报告</el-button>
            </el-button-group>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        loading:false,
        listLoading:false,
        filters:{
          name:''
        },
        caseResultList:[]
      }
    },
    methods:{
      getCaseResultList(){
        this.caseResultList = [{name:'Test'}]
      }
    },
    mounted(){
      this.getCaseResultList()
    }
  }
</script>