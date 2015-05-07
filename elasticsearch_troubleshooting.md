# elasticsearch问题排查方法探讨

## 发现问题原因的途径

*	_cluster/health

*	elasticsearch log (最重要的是master的Debug, Warn, Error log)

*	_nodes/stats或者_nodes/< specific_node_ip_or_id >/stats

*	_nodes/hot_threads或者_nodes/< specific_node_ip_or_id >/hot_threads

---
> Written with [StackEdit](https://stackedit.io/).