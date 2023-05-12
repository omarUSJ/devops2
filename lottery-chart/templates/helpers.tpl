{{/* Returns the full name of the chart, including the release name */}}
{{- define "lottery.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name }}
{{- end }}

{{/* Returns the name of the chart */}}
{{- define "lottery.chartName" -}}
{{- printf "%s" .Chart.Name }}
{{- end }}

{{/* Returns the name of the database deployment */}}
{{- define "lottery.databaseName" -}}
{{- printf "%s-database" (include "lottery.fullname" .) }}
{{- end }}

{{/* Returns the name of the application deployment */}}
{{- define "lottery.appName" -}}
{{- printf "%s-app" (include "lottery.fullname" .) }}
{{- end }}

{{/* Returns the name of the PVC */}}
{{- define "lottery.persistence.claimName" -}}
{{- printf "%s-pvc" (include "lottery.fullname" .) }}
{{- end }}

{{/* Returns the values of a secret */}}
{{- define "lottery.secret" -}}
{{- printf "%s" (index .Values.secrets .) }}
{{- end }}

{{/* Returns the values of a config map */}}
{{- define "lottery.configMap" -}}
{{- printf "%s" (index .Values.configMaps .) }}
{{- end }}

{{- define "lottery.service.port" -}}
{{- default 80 .Values.lottery.service.port | int -}}
{{- end -}}
