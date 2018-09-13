import Vue from 'vue'
import Router from 'vue-router'
import CaseBase from '@/components/case/CaseBase'
import Home from '@/components/Home'
import OrgBase from '@/components/member/OrgBase'
import ProjectBase from '@/components/project/ProjectBase'
import AgentBase from '@/components/agent/AgentBase'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      component:()=>import('@/components/common/Login')
    },
    {
      path:'/home',
      component:Home,
      name:'首页',
      children:[
        {
          path:'/me',
          name:'工作台',
          component:()=>import('@/components/home/me')
        },
        {
          path:'/orgbase',
          name:'组织',
          component:OrgBase,
          children:[
            {
              path:'/org',
              name:'部门',
              component:()=>import('@/components/member/Org')
            },{
              path:'/org/member',
              name:'人员',
              component:()=>import('@/components/member/Member')
            },{
              path:'/org/role',
              name:'角色',
              component:()=>import('@/components/auth/Role')
            }
          ]
        },
        {
          path:'/project',
          name:'项目管理',
          component:()=>import('@/components/project/Project')
        },
        {
          path:'/base',
          component:ProjectBase,
          children:[
            {
              path:'/module/:id',
              name:'维护模块',
              component:()=>import('@/components/project/ProjectModule')
            },{
              path:'/code/:id',
              name:'状态码',
              component:()=>import('@/components/project/ProjectCode')
            },{
              path:'/host/:id',
              name:'环境管理',
              component:()=>import('@/components/project/Host')
            },
            {
              path:'/log/:id',
              name:'项目动态',
              component:()=>import('@/components/project/ProjectLog')
            },
            {
              path:'/projectmember/:id',
              name:'项目人员',
              component:()=>import('@/components/project/ProjectMember')
            },
            {
              path:'/api/list/:id',
              component:()=>import('@/components/project/api/ApiList')
            },
            {
              path:'/api/add/:id',
              component:()=>import('@/components/project/api/ApiAdd')
            }
          ]
        },
        {
          name:'用例管理',
          path:'/casebase',
          component:CaseBase,
          children:[
            {
              path:'/case',
              name:'用例管理',
              component:()=>import('@/components/case/Case')
            },
            {
              path:'/case/api',
              name:'用例API',
              component:()=>import('@/components/case/CaseApi')
            },
            {
              path:'/case/group',
              name:'分组',
              component:()=>import('@/components/case/CaseGroup')
            },
            {
              path:'/case/script',
              name:'脚本',
              component:()=>import('@/components/case/Script')
            },
            {
              path:'/case/result',
              name:'结果',
              component:()=>import('@/components/case/CaseResult')
            },
            {
              path:'/case/mock',
              name:'数据',
              component:()=>import('@/components/case/Mock')
            }
          ]
        },
        {
          path:'/help',
          name:'帮助',
          component:()=>import('@/components/Help')
        },{
          path:'/agentbase',
          name:'代理',
          component:AgentBase,
          children:[
            {
              path:'/agent',
              name:'代理',
              component:()=>import('@/components/agent/Agent')
            }
          ]
        },{
          path:'/profile',
          name:'个人信息',
          component:()=>import('@/components/common/Profile')
        },{
          path:'/message',
          name:'消息',
          component:()=>import('@/components/Message')
        },{
          path:'/timeline',
          name:'图',
          component:()=>import('@/components/TimeLine')
        }
      ]
    }
  ]
})
