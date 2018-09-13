<template>
  <el-row>
    <el-col :span="24">
      <el-button type="primary" @click="addApi">添加接口</el-button>
      <el-button type="primary" @click="addScript">添加等待</el-button>
      <el-button type="primary" @click="goCase">返回用例</el-button>
      <el-table :data="taskApiList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="order" label="顺序" sortable>
          <template slot-scope="scope">
            <el-button-group>
            <el-button icon="el-icon-upload2" circle></el-button>
            <el-button icon="el-icon-download" circle></el-button>
          </el-button-group>
          </template>
        </el-table-column>
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column prop="action" label="行为" sortable></el-table-column>
        <el-table-column prop="result" label="测试结果" sortable>
          <template slot-scope="scope">
            <span v-show="!scope.row.result&&!scope.row.testStatus">尚无测试结果</span>
            <span v-show="scope.row.testStatus">测试中...</span>
            <span v-show="scope.row.result==='success'&&!scope.row.testStatus" @click="resultShow(scope.row)">成功,查看详情</span>
            <span v-show="scope.row.result==='fail'&&!scope.row.testStatus" @click="resultShow(scope.row)">失败,查看详情</span>
            <span v-show="scope.row.result==='timeout'&&!scope.row.testStatus" @click="resultShow(scope.row)">请求超时</span>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="testApi(scope.$index, scope.row)">测试</el-button>
            <router-link :to="'/api/add'">
                <el-button>修改</el-button>
            </router-link>
            <el-button @click="delApi(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title="选择API" :visible.sync="addApiListVisible" :close-on-click-modal="false" >
        <el-row>
            <el-col :span="18">
                <el-table :data="searchApiList" highlight-current-row v-loading="apiListLoading">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column prop="name" label="名称" min-width="25%" sortable>
                    </el-table-column>
                    <el-table-column prop="requestType" label="HTTP方式" min-width="15%" sortable>
                    </el-table-column>
                    <el-table-column prop="apiAddress" label="地址" min-width="60%" sortable>
                    </el-table-column>
                </el-table>
            </el-col>
        </el-row>
        <el-col :span="24" class="toolbar">
            <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
        </el-col>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addApiListVisible = false">取消</el-button>
            <el-button type="primary" @click="addApiForm">提交</el-button>
        </div>
      </el-dialog>
      <el-dialog title="设置等待时间" :visible.sync="addScriptVisible" :close-on-click-modal="false" >
        <el-form label-width="80px">
          <el-form-item label='等待时间'>  
            <el-input type='text' auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addScriptVisible = false">取消</el-button>
            <el-button @click="addScriptForm">提交</el-button>
          </div>
      </el-dialog>
    </el-col>
  </el-row>
</template>

<script>
export default {
    data() {
        return{
          total:0,
          listLoading:false,
          apiListLoading:false,
          addApiListVisible:false,
          addScriptVisible:false,
          taskApiList:[],
          searchApiList:[]
        }
      },
      methods:{
        delApi(index,row){},
        testApi(index,row){},
        resultShow(row){},
        getTaskApiList(){
          this.taskApiList = [{}]
        },
        addApi(){
          this.addApiListVisible=true
          let _this = this
          _this.ajax.get("/static/mock/apilist.json").then(function(res){
            _this.searchApiList = res.data.result.data
          })
        },
        addApiForm(){
          this.addApiListVisible=false
        },
        addScript(){
          this.addScriptVisible=true
        },
        addScriptForm(){
          this.addScriptVisible=false
        },
        goCase(){
          this.$router.push('/case')
        }
      },
      mounted(){
        this.getTaskApiList()
      }
    }
</script>